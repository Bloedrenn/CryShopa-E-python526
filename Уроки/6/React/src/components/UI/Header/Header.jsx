// import './Header.css'
import styles from './Header.module.css'

const Header = ({ text: myText, title = "Заголовок" }) => (
  <header className={styles.header}>
    <p>{myText}</p>
    <p>{title}</p>
  </header>
)


export default Header
