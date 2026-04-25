import styles from './ItemCard.module.css'


const ItemCard = ({ item }) => (
  <div className={styles.item}>
    <strong>{item.name}</strong>
    <div>{item.description}</div>
    <div>{item.isAvailable ? 'В наличии :)' : 'Нет в наличии :('}</div>
  </div>
)

export default ItemCard
