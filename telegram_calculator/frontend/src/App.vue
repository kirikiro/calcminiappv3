<!-- frontend/src/App.vue -->
<template>
  <div id="calculator">
    <CalculatorDisplay :value="displayValue" />
    
    <div class="button-grid">
      <!-- Проходимся по массиву кнопок и рендерим их -->
      <CalculatorButton
        v-for="button in buttons"
        :key="button.label"
        :label="button.label"
        :type="button.type"
        @click="handleButtonClick"
      />
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import CalculatorDisplay from './components/CalculatorDisplay.vue';
import CalculatorButton from './components/CalculatorButton.vue';

// Инициализируем Telegram Web App
onMounted(() => {
  if (window.Telegram && window.Telegram.WebApp) {
    window.Telegram.WebApp.ready();
  }
});

// --- Состояние калькулятора ---
const displayValue = ref('0'); // Значение, которое отображается на дисплее
const firstOperand = ref(null); // Первый операнд
const operator = ref(null);     // Текущий оператор
const waitingForSecondOperand = ref(false); // Флаг, указывающий на ожидание второго операнда

// --- Описание кнопок ---
// Используем массив объектов, чтобы легко управлять кнопками
const buttons = ref([
  { label: 'C', type: 'action' }, { label: 'sin', type: 'action' }, { label: 'cos', type: 'action' }, { label: '÷', type: 'operator' },
  { label: '7' }, { label: '8' }, { label: '9' }, { label: '×', type: 'operator' },
  { label: '4' }, { label: '5' }, { label: '6' }, { label: '−', type: 'operator' },
  { label: '1' }, { label: '2' }, { label: '3' }, { label: '+', type: 'operator' },
  { label: '0' }, { label: '.' }, { label: '√', type: 'action' }, { label: '=', type: 'operator' },
]);


// --- Логика калькулятора ---

/**
 * Основная функция-обработчик нажатий на кнопки.
 * @param {string} label - Текст нажатой кнопки.
 */
const handleButtonClick = (label) => {
  if (isFinite(Number(label)) || label === '.') {
    inputDigit(label);
  } else if (label === 'C') {
    resetCalculator();
  } else if (['sin', 'cos', '√'].includes(label)) {
    performUnaryOperation(label);
  } else if (label === '=') {
    performCalculation();
  } else {
    handleOperator(label);
  }
};

/**
 * Ввод цифры или точки.
 * @param {string} digit - Введенная цифра или точка.
 */
const inputDigit = (digit) => {
  if (waitingForSecondOperand.value) {
    displayValue.value = digit;
    waitingForSecondOperand.value = false;
  } else {
    if (displayValue.value === '0' && digit !== '.') {
      displayValue.value = digit;
    } else if (!displayValue.value.includes('.') || digit !== '.') {
      displayValue.value += digit;
    }
  }
};

/**
 * Обработка операторов (+, -, ×, ÷).
 * @param {string} nextOperator - Нажатый оператор.
 */
const handleOperator = (nextOperator) => {
  const inputValue = parseFloat(displayValue.value);

  if (operator.value && waitingForSecondOperand.value) {
    operator.value = nextOperator;
    return;
  }

  if (firstOperand.value === null) {
    firstOperand.value = inputValue;
  } else if (operator.value) {
    const result = performCalculation();
    displayValue.value = String(result);
    firstOperand.value = result;
  }

  waitingForSecondOperand.value = true;
  operator.value = nextOperator;
};

/**
 * Выполнение бинарной операции.
 * @returns {number|null} Результат вычисления.
 */
const performCalculation = () => {
  if (operator.value === null || waitingForSecondOperand.value) return;

  const secondOperand = parseFloat(displayValue.value);
  const operations = {
    '+': (a, b) => a + b,
    '−': (a, b) => a - b,
    '×': (a, b) => a * b,
    '÷': (a, b) => a / b,
  };

  if (!operations[operator.value]) return;
  
  const result = operations[operator.value](firstOperand.value, secondOperand);
  
  displayValue.value = String(result);
  firstOperand.value = null;
  operator.value = null;
  waitingForSecondOperand.value = false;

  return result;
};

/**
 * Выполнение унарной операции (sin, cos, √).
 * @param {string} operation - Название операции.
 */
const performUnaryOperation = (operation) => {
    const value = parseFloat(displayValue.value);
    let result = 0;
    
    switch (operation) {
        case 'sin':
            // Math.sin работает с радианами, конвертируем градусы в радианы
            result = Math.sin(value * (Math.PI / 180));
            break;
        case 'cos':
            // Math.cos работает с радианами
            result = Math.cos(value * (Math.PI / 180));
            break;
        case '√':
            result = Math.sqrt(value);
            break;
    }
    // Округляем результат для большей наглядности
    displayValue.value = String(Number(result.toPrecision(10)));
};


/**
 * Сброс состояния калькулятора.
 */
const resetCalculator = () => {
  displayValue.value = '0';
  firstOperand.value = null;
  operator.value = null;
  waitingForSecondOperand.value = false;
};

</script>

<style>
/* Глобальные стили */
body {
  margin: 0;
  background-color: #000;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
}

#calculator {
  display: flex;
  flex-direction: column;
  height: 100vh;
  padding: 10px;
  box-sizing: border-box;
}

.button-grid {
  display: grid;
  /* 4 колонки равной ширины */
  grid-template-columns: repeat(4, 1fr);
  gap: 10px; /* Промежутки между кнопками */
  flex-grow: 1;
}
</style>