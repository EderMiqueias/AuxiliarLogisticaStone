import './assets/styles/App.css';
import "./assets/styles/Card.css";


import Navbar from './components/template/Navbar';
import Polos from './components/template/Polos';

export default () => {
    return (
        <div className="App">
            <Navbar />
            <Polos className="Polos"/>
        </div>
    );
}
