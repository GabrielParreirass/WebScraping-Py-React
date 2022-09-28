import './App.css';
import Axios from 'axios'
import { useEffect, useState } from 'react';


function App() {

  const[data, setData] = useState('')

  useEffect(()=>{
   Axios.get('http://127.0.0.1:5000/api').then((res)=>{
    setData(res.data)
    console.log(res)
   })
  },[])


  return (
    <div>{data}</div>
  );
}

export default App;
