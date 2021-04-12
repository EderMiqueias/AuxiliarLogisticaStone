import '../assets/styles/App.css';
import "../assets/styles/Card.css";


import Navbar from '../components/template/Navbar';
import Footer from '../components/template/Footer';
import Routes from './Routes'

const App = () => {
    return (
        <div className="App">
            <Navbar />
            <Routes />
            <Footer />
        </div>
    );
}

export default App;
