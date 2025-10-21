<template>
  <div class="calculator-display">
    {{ value }}
  </div>
</template>

<script setup>
// Определяем входной параметр `value`
defineProps({
  value: {
    type: String,
    required: true
  }
});
</script>

<style scoped>
/* Стили для дисплея калькулятора */
.calculator-display {
  background-color: #1c1c1c;
  color: white;
  font-size: 3rem;
  padding: 20px;
  text-align: right;
  border-radius: 8px;
  margin-bottom: 10px;
  overflow-x: auto; /* Горизонтальная прокрутка, если число не помещается */
  white-space: nowrap;
}
</style>