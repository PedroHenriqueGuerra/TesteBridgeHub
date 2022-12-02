
import { Link } from 'react-router-dom'
import './card.css'


function Investir(){
  return(
        <div className='card-centralizar'>
            <div className='card-container'>
                <div className='image-container'>
                    <img src={''} />
                </div> 
                <div className='card-content'>
                    <div  className='card-title'>
                        <h3>{'Emprese '}</h3>
                    </div>
                    <div className='card-body'>
                        <p>{'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Pretium lectus quam id leo. Diam in arcu cursus euismod quis viverra nibh cras pulvinar. Vitae suscipit tellus mauris a diam maecenas. Sodales neque sodales ut etiam sit. '}</p>
                    </div>
                </div>
                <div className='btn'>
                    <button>
                        <a>
                            <Link className='card' to="/Investimentos/detalhes">Detalhes</Link> 
                        </a>
                    </button>
                </div>
            </div>
        </div>
  )
}



export default Investir;