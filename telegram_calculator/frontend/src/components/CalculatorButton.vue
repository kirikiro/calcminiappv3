<!-- frontend/src/components/CalculatorButton.vue -->
<template>
  <button 
    class="calculator-button"
    :class="buttonClass"
    @click="handleClick"
  >
    {{ label }}
  </button>
</template>

<script setup>
import { computed } from 'vue';

// Определяем входные параметры (props) для компонента
const props = defineProps({
  label: {
    type: String,
    required: true
  },
  type: {
    type: String,
    default: 'default' // 'default', 'operator', 'action'
  }
});

// Определяем событие, которое компонент может отправлять родителю
const emit = defineEmits(['click']);

// Вычисляемое свойство для определения CSS-класса кнопки
const buttonClass = computed(() => {
  if (props.type === 'operator') return 'operator-button';
  if (props.type === 'action') return 'action-button';
  return '';
});

// Функция, вызываемая при клике на кнопку
const handleClick = () => {
  // Отправляем событие 'click' родителю, передавая значение кнопки
  emit('click', props.label);
};
</script>

<style scoped>
/* Стили для кнопки */
.calculator-button {
  width: 100%;
  height: 60px;
  font-size: 1.5rem;
  border: 1px solid #333;
  border-radius: 8px;
  background-color: #505050;
  color: white;
  cursor: pointer;
  transition: background-color 0.2s;
}

.calculator-button:hover {
  background-color: #6a6a6a;
}

.calculator-button:active {
  background-color: #818181;
}

.operator-button {
  background-color: #ff9500; /* Оранжевый для операторов */
}
.operator-button:hover {
  background-color: #ffab3e;
}
.operator-button:active {
  background-color: #ffc27a;
}

.action-button {
  background-color: #d4d4d2; /* Светло-серый для действий */
  color: #1c1c1c;
}
.action-button:hover {
  background-color: #e2e2e1;
}
.action-button:active {
  background-color: #f0f0ef;
}
</style>