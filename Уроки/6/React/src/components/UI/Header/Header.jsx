import './Header.css'

const Header = ({ text: myText, title = "Заголовок" }) => (
  <header className="header">
    <p>{myText}</p>
    <p>{title}</p>
  </header>
)


export default Header
