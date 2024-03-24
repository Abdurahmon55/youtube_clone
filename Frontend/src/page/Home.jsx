import React from 'react'
import VideoCard from '../components/card/VideoCard'
import MinNav from '../components/navbar/MinNav'

function Home() {
  return (
    <div className='pl-24 mt-4'>
        <MinNav/>
        <VideoCard/>
    </div>
  )
}

export default Home