import React from 'react'
import { RxHamburgerMenu } from "react-icons/rx";
import { FaYoutube } from "react-icons/fa";
import { MdOutlineMic } from "react-icons/md";
import { IoIosSearch } from "react-icons/io";
import { IoVideocamOutline } from "react-icons/io5";
import { PiBellRingingThin } from "react-icons/pi";
function Navbar() {
  return (
    <div className='grid grid-cols-12 mt-2'>
        <div className='flex  items-center gap-8 text-lg col-span-3'>
            <i className='hover:bg-slate-200 p-1 rounded-full cursor-pointer'><RxHamburgerMenu /></i>
            <div className='flex items-center gap-2 cursor-pointer'>
                <i className='text-red-500 text-2xl'><FaYoutube /></i>
                <span className='font-semibold'>YouTube</span>
            </div>
        </div>
        <div className='flex items-center col-span-6 px-2'>
            <input type="text" className='px-4 border hidden sm:block p-1 w-full border-slate-500 rounded-l-full ' placeholder='serach'/>
            <i className='border p-2 hidden sm:block border-l-gray-100 border-slate-500 rounded-r-full px-4 bg-gray-100 hover:bg-gray-200 cursor-pointer'><IoIosSearch /></i>
            <i className='text-2xl sm:hidden w-full  flex justify-end'><IoIosSearch /></i>
            <i className='bg-gray-300 p-1 rounded-full ml-4 hover:bg-gray-400 cursor-pointer'><MdOutlineMic /></i>
        </div>
        <div className='text-xl flex gap-4 items-center col-span-3  ml-auto'>
            <i><IoVideocamOutline /></i>
            <i><PiBellRingingThin /></i>
            <span className='font-bold text-lg bg-indigo-800 rounded-full px-3 pb-2 text-white'>a</span>
        </div>
    </div>
  )
}

export default Navbar