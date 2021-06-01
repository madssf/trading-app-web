import React from 'react';
import * as FaIcons from 'react-icons/fa';
import * as AiIcons from 'react-icons/ai';
import * as IoIcons from 'react-icons/io';
import * as RiIcons from 'react-icons/ri';

export const SidebarData = [
  {
    title: 'Home',
    path: '/home',
    icon: <AiIcons.AiFillHome />,
    iconClosed: <RiIcons.RiArrowDownSFill />,
    iconOpened: <RiIcons.RiArrowUpSFill />,

    subNav: [
      {
        title: 'Portfolios',
        path: '/my_portfolios',
        icon: <IoIcons.IoIosPaper />
      },
      {
        title: 'Watchlists',
        path: '/home/watchlists',
        icon: <IoIcons.IoIosPaper />
      }
    ]
  },
  {
    title: 'Explore',
    path: '/explore',
    icon: <AiIcons.AiOutlineCompass />,
    iconClosed: <RiIcons.RiArrowDownSFill />,
    iconOpened: <RiIcons.RiArrowUpSFill />,

    subNav: [
      {
        title: 'Portfolios',
        path: '/explore/portfolios',
        icon: <IoIcons.IoIosPaper />,
        cName: 'sub-nav'
      },
      {
        title: 'Watchlists',
        path: '/explore/watchlists',
        icon: <IoIcons.IoIosPaper />,
        cName: 'sub-nav'
      },
      {
        title: 'Currencies',
        path: '/explore/currencies',
        icon: <IoIcons.IoIosPaper />
      }
    ]
  },
  {
    title: 'Research',
    path: '/research',
    icon: <RiIcons.RiMicroscopeLine />
  },
  {
    title: 'Guide',
    path: '/guide',
    icon: <RiIcons.RiBookLine />
  },
  {
    title: 'Log out',
    path: '/logout',
    icon: <AiIcons.AiOutlineLogout />
  },

  
  

];
