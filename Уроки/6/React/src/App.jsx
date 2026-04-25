import { useState, useEffect } from 'react'
import axios from 'axios'

import AddItem from '@components/Items/Forms/AddItem'
import Header from '@components/UI/Header'
import ItemList from '@components/Items/ItemList'

import styles from './App.module.css'

const API_URL = import.meta.env.VITE_API_URL


function App() {
  // items = [
  //   {id: "1", name: "Xiaomi Redmi 10", description: "Топ за свои деньги!", isAvailable: true},
  //   {id: "2", name: "Iphone X", description: "Крутой телефон (нет) и дорогой (да)", isAvailable: false},
  //   {id: "3", name: "Tesla Model Y", description: "Новая, купил вчера", isAvailable: true}
  // ]
  const [items, setItems] = useState([])
  const [itemsLoading, setItemsLoading] = useState(true)
  const [itemsError, setItemsError] = useState(null)

  useEffect(() => {
    axios.get(`${API_URL}/items`)
      .then(response => {
        setItems(response.data)
        setItemsLoading(false)
      })
      .catch(error => {
        console.error(error)
        setItemsLoading(false)

        const errMsg = (
          error.message === "Network Error" ? "Ошибка сети"
          : error.message === "Request failed with status code 404" ? "Ресурс не найден" // Можно так: error.response.status === 404
          : "Повторите попытку позже"
        )
        setItemsError(`Ошибка загрузки вещей: ${errMsg}`)
      })
  }, [])

  const addItem = (newItem) => {
    ///// {name: "Tesla Model Y", description: "Новая, купил вчера", isAvailable: true}
    axios.post(`${API_URL}/items`, newItem)
      .then(response => setItems([...items, response.data]))
  }

  return (
    <>
      <Header />

      <main className={styles.main}>
        <ItemList
          items={items}
          itemsLoading={itemsLoading}
          itemsError={itemsError}
        />
      </main>
      <aside className={styles.aside}>
        <AddItem onAdd={addItem} />
      </aside>
    </>
  )
}

export default App
