import { BrowserRouter, Routes, Route} from 'react-router-dom';

import Home from './pages/Home';
import Investimento from './pages/Investimentos';
import Header from './components/Header';
import Detalhes from './pages/Investimentos/detalhes';

function RoutesApp(){
    return(
        <BrowserRouter>
        <Header/>
            <Routes>
                <Route path="/" element={<Home/>} />
                <Route path="/Investimentos" element={<Investimento/>} />
                <Route path='/Investimentos/detalhes' element={<Detalhes/>} />
            </Routes>
        </BrowserRouter>
    )
}

export default RoutesApp;