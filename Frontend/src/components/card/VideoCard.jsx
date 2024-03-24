import React from 'react'
import imgs from '../../image/download.jpg'
import defaul from '../../image/download (3).jpg'

function VideoCard() {
    const data = [
        { image: imgs, name: 'Сагындым Жаным', media: 'Music Time', like: 120, id: 1, },
        { image: imgs, name: 'Сагындым Жаным', media: 'Music Time', like: 120, id: 2, },
        { image: imgs, name: 'Сагындым Жаным', media: 'Music Time', like: 120, id: 3, },
        { image: imgs, name: 'Сагындым Жаным', media: 'Music Time', like: 120, id: 4, },
        { image: imgs, name: 'Сагындым Жаным', media: 'Music Time', like: 120, id: 5, },
        { image: imgs, name: 'Сагындым Жаным', media: 'Music Time', like: 120, id: 6, },
        { image: imgs, name: 'Сагындым Жаным', media: 'Music Time', like: 120, id: 7, },
        { image: imgs, name: 'Сагындым Жаным', media: 'Music Time', like: 120, id: 8, },
        { image: imgs, name: 'Сагындым Жаным', media: 'Music Time', like: 120, id: 9, },
        { image: imgs, name: 'Сагындым Жаным', media: 'Music Time', like: 120, id: 10, },
        { image: imgs, name: 'Сагындым Жаным', media: 'Music Time', like: 120, id: 11, },
        { image: imgs, name: 'Сагындым Жаным', media: 'Music Time', like: 120, id: 12, },
    ]
    return (
        <div className='mt-4'>
            <div className='grid grid-cols-12 gap-4'>
                {data.map((item) => (
                    <div key={item.id} className='lg:col-span-3 md:col-span-4 sm:col-span-6 col-span-12 bg-slate-100 p-1 rounded-lg'>
                        <img className='rounded-lg w-full cursor-pointer' src={item.image} alt="" />
                        <div className='mt-2 flex gap-2'>
                            <img className='w-8 h-8 rounded-full cursor-pointer' src={defaul} alt="" />
                            <div>
                                <h2 className='k font-semibold cursor-pointer'>{item.name} </h2>
                                <span className='text-xs font-semibold text-gray-500 cursor-pointer'>{item.media}</span>
                                <div className='flex items-center gap-1 cursor-pointer'>
                                    <span className='text-xs font-semibold text-gray-500'>{item.like} ming marta</span>
                                    <span className=' bg-gray-500 w-1 h-1 rounded-full'></span>
                                    <span className='text-xs font-semibold text-gray-500'>2 kun oldin</span>
                                </div>
                                
                            </div>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    )
}

export default VideoCard