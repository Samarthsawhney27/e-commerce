import { Home } from './pages/Home';

function App() {
  return (
    <>
      <header className="main-header">
        <div className="container">
          <h1 className="logo">Demo E-Commerce</h1>
          <button className="btn btn-primary">Cart (0)</button>
        </div>
      </header>
      <main className="container">
        <Home />
      </main>
    </>
  )
}
export default App;
