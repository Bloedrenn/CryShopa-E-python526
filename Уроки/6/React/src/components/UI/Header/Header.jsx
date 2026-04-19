import { useEffect } from 'react'

import styles from './Header.module.css'


const Header = ({ text: myText, title = "Заголовок" }) => {
  useEffect(
    () => { // можно убрать {}
      return () => console.log("Header демонтировался") // Функция очистки (cleanup)
    },
    []
    // Важно указать []. Иначе получим 2 лога в консоли.
    // Эффект выполняется только один раз при монтировании компонента.
    // При последующих рендерах (rerender) эффект НЕ запускается снова, поэтому cleanup не вызывается.
    // Cleanup выполнится только один раз — при размонтировании компонента.
  )

  return (
    <header className={styles.header}>
      <p>{myText}</p>
      <p>{title}</p>
    </header>
  )
}


export default Header
