import { useState } from 'react'


function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <h1>Счётчик кликов</h1>
      <button onClick={() => setCount(count + 1)}>
        Клик: {count}
      </button>
    </>
  )
}

export default App
