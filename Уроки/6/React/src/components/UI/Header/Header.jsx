const Header = ({ text: myText, title = "Заголовок" }) => (
  <header>
    <p>{myText}</p>
    <p>{title}</p>
  </header>
)


export default Header
