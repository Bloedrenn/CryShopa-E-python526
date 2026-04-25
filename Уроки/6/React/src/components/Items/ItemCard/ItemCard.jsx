import { BsTrash3Fill } from "react-icons/bs"
import { FaEdit } from "react-icons/fa"

import styles from './ItemCard.module.css'


const ItemCard = ({ item }) => (
  <div className={styles.item}>
    <BsTrash3Fill
      title="Удалить"
      className={styles.deleteIcon}
      size={30}
      color="red"
    />
    <FaEdit
      title="Редактировать"
      className={styles.editIcon}
      size={35}
      color="#000"
    />
    <strong>{item.name}</strong>
    <div>{item.description}</div>
    <div>{item.isAvailable ? 'В наличии :)' : 'Нет в наличии :('}</div>
  </div>
)

export default ItemCard
