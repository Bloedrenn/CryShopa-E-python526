import { useState, useEffect } from 'react'
import axios from 'axios'

import Header from '@components/UI/Header'

const API_URL = import.meta.env.VITE_API_URL


function App() {
  // items = [
  //   {id: "1", name: "Xiaomi Redmi 10", description: "Топ за свои деньги!", isAvailable: true},
  //   {id: "2", name: "Iphone X", description: "Крутой телефон (нет) и дорогой (да)", isAvailable: false}
  // ]
  const [items, setItems] = useState([])
  const [itemsLoading, setItemsLoading] = useState(true)

  useEffect(() => {
    axios.get(`${API_URL}/items`)
      .then(response => {
        setItems(response.data)
        setItemsLoading(false)
      })
      .catch(error => {
        console.error(error)
        setItemsLoading(false)
      })
  }, [])

  // Лучше не писать условие itemsLoading здесь - перед основным return'ом

  return (
    <>
      <Header />

      <h1>Список вещей</h1>
      <ul>
        {
          itemsLoading ? (
            <div>Загрузка вещей...</div>
          ) : (
            items.map(item => (
              <li key={item.id}>
                <strong>{item.name}</strong>: {item.description} - {item.isAvailable ? "В наличии" : "Нет в наличии"}
              </li>
            ))
          )
        }
      </ul>
    </>
  )
}

export default App
