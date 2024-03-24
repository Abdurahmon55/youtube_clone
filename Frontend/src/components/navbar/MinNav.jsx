import React from 'react'
import { NavLink } from 'react-router-dom'

function MinNav() {
    const data = [
        { title: 'hammsi', id: 1 },
        { title: 'mikslar', id: 2 },
        { title: 'musiqa', id: 3 },
        { title: 'jonli', id: 4 },
        { title: 'Pazondalik', id: 5 },
        { title: 'tomosha qilingan', id: 6 },
    ]
    return (
        <div>
            <div className='flex gap-4 '>
                {data.map((item) => (
                    <NavLink key={item.id}>
                         <span className='hover:bg-gray-400 text-nowrap bg-gray-300 font-semibold rounded-md px-2 p-1'>{item.title}</span>
                    </NavLink>
                ))}
            </div>
        </div>
    )
}

export default MinNav