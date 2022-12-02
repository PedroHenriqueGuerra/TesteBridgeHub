import './header.css'
import { Link } from 'react-router-dom' 

function Header(){
    return(
        <header>
            <Link className='logo' to="/">Bridge</Link>
            <Link className='investimentos' to="/investimentos">Investimentos</Link>
        </header>
    )
}

export default Header