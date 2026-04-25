import { useState, useRef } from 'react'

import styles from './AddItem.module.css'


const AddItem = ({ onAdd }) => {
  const [name, setName] = useState("")
  const [description, setDescription] = useState("")
  const [isAvailable, setIsAvailable] = useState(false)

  // Создаем ref для формы
  const itemAddForm = useRef(null)

  return (
    <form className={styles.form} ref={itemAddForm}>
      <input
        type="text"
        placeholder='Название'
        onChange={e => setName(e.target.value)}
      />
      <textarea
        placeholder='Описание'
        onChange={e => setDescription(e.target.value)}
      ></textarea>

      <div>
        <input
          type='checkbox'
          id='isAvailable'
          onChange={e => setIsAvailable(e.target.checked)}
        />
        <label htmlFor='isAvailable'>В наличии?</label>
      </div>

      <button
        type='button'
        onClick={() => {
          onAdd({ name, description, isAvailable })

          // Сбрасываем поля формы
          itemAddForm.current.reset()
        }}
      >
        Добавить
      </button>
    </form>
  )
}

export default AddItem