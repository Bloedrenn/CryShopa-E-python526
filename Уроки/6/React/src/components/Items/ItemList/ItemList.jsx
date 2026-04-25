import ItemCard from '@components/Items/ItemCard'


const ItemList = ({ items, itemsLoading, itemsError }) => {
  return (
    <>
      <h1>Список вещей</h1>
      <div>
        {
          itemsLoading ? (
            <div className="spinner-border" role="status">
              <span className="visually-hidden">Загрузка вещей...</span>
            </div>
          ) : itemsError ? (
            <div>{itemsError}</div>
          ) : items.length !== 0 ? (
            items.map(item => (
              <ItemCard key={item.id} item={item} />
            ))
          ) : (
            <div>Вещей ещё нет</div>
          )
        }
      </div>
    </>
  )
}

export default ItemList