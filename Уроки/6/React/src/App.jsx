import { useState, useEffect } from 'react'

import Header from '@components/UI/Header'
import Image from '@components/Image'

import carImgUrl from './images/car.png'


function App() {
  const [count, setCount] = useState(0)
  const [tempText, setTempText] = useState("Hello World!")
  const [userText, setUserText] = useState("")
  const [showFirstHeader, setShowFirstHeader] = useState(true)

  useEffect(
    () => {
      document.title = `Вы нажали ${count} раз`
    },
    [count]
  )
  // Функция в таком варианте useEffect вызывается: 1. При монтировании компонента. 2. При повторном рендере компонента который вызван изменением count.

  const pHover = () => { 
    console.log("Навели на p")
    console.log("Я БОЛЬШАЯ ФУНКЦИЯ")
    console.log("Я БОЛЬШАЯ ФУНКЦИЯ")
    console.log("Я БОЛЬШАЯ ФУНКЦИЯ")
    console.log("ВО МНЕ МНОГО СТРОЧЕК КОДА")
    console.log("ВО МНЕ МНОГО СТРОЧЕК КОДА")
    setTempText(10)
  }

  return (
    <>
      {showFirstHeader && <Header text="Шапка сайта" title="ХЕЛЛО" />}
      <button onClick={() => setShowFirstHeader(!showFirstHeader)}>{showFirstHeader ? "Скрыть" : "Показать"} первый Header</button>

      <p onMouseEnter={pHover}>Hello World</p>
      <h1>Счётчик кликов</h1>
      <button onClick={() => setCount(count + 1)}>
        Клик: {count}
      </button>
      <Header text="МОН" /> {/* Для примера */}

      {/* 1 способ */}
      {/* <img src="https://assets.avtocod.ru/storage/images/articles-2022/otnyud-ne-bmw-top-10-samykh-dorogikh-mashin-mira-v-2022-godu/otnyud-ne-bmw-top-10-samykh-dorogikh-mashin-mira-v-2022-godu-3-min.jpg" /> */}

      {/* 2 способ */}
      {/* <img src={carImgUrl} /> */}

      {/* 3 способ */}
      <Image imageUrl={carImgUrl} />
      {tempText}

      <div>Вы ввели: {userText}</div>
      <input onChange={event => setUserText(event.target.value)} /> {/* Если нужен change как в html, то нужно использовать onBlur */}
    </>
  )
}

export default App
