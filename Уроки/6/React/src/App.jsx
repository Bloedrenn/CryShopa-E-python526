import AddItem from '@components/Items/Forms/AddItem'
import Header from '@components/UI/Header'
import ItemList from '@components/Items/ItemList'

import styles from './App.module.css'


function App() {
  return (
    <>
      <Header />

      <main className={styles.main}>
        <ItemList />
      </main>
      <aside className={styles.aside}>
        <AddItem />
      </aside>
    </>
  )
}

export default App
