import { useState } from 'react'

import Header from '@components/UI/Header'


function App() {
  const [count, setCount] = useState(0)

  const pHover = () => { 
    console.log("Навели на p")
    console.log("Я БОЛЬШАЯ ФУНКЦИЯ")
    console.log("Я БОЛЬШАЯ ФУНКЦИЯ")
    console.log("Я БОЛЬШАЯ ФУНКЦИЯ")
    console.log("ВО МНЕ МНОГО СТРОЧЕК КОДА")
    console.log("ВО МНЕ МНОГО СТРОЧЕК КОДА")
  }

  return (
    <>
      <Header text="Шапка сайта" title="ХЕЛЛО" />
      <p onMouseEnter={pHover}>Hello World</p>
      <h1>Счётчик кликов</h1>
      <button onClick={() => setCount(count + 1)}>
        Клик: {count}
      </button>
      <Header text="МОН" title="ЛУНА" /> {/* Для примера */}
    </>
  )
}

export default App
