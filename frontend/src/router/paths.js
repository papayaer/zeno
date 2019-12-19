/**
 * Define all of your application routes here
 * for more information on routes, see the
 * official documentation https://router.vuejs.org/en/
 */

export default [
  {
    path: '/',
    component: () => import('@/views/Home'),
    children: [
      { path: '', name: 'home', component: () => import('@/views/Discovery')},
      { path: '/explore', name: 'explore', component: () => import('@/views/Explore')},
      // { path: '/post/:postid/single', name: 'single', component: () => import('@/views/Single'),props: true},
      { path: '/test', name: 'test', component: () => import('@/views/Test')},
      { path: '/about', name: 'about', component: () => import('@/views/About')},
    ]
  },{
    path: '/user/:author/index',
    component: () => import('@/views/User'),
    children: [
      { path: '',component: () => import('@/components/tab/Dynamic'), props: true },
      { path: '/user/:author/index', component: () => import('@/components/tab/Dynamic'), props: true },
      { path: '/user/:author/fans', component: () => import('@/components/tab/FansPage'), props: true },
      { path: '/user/:author/followed', component: () => import('@/components/tab/FollowedPage'), props: true  },
      { path: '/user/:author/favorite', component: () => import('@/components/tab/Favorite'), props: true  },
      { path: '/user/:author/talk', component: () => import('@/components/tab/TalkPage'), props: true  },
      { path: '/user/:author/history', component: () => import('@/components/tab/History'), props: true  },
      { path: '/user/:author/plan', component: () => import('@/components/tab/Plan'), props: true  },
      { path: '/user/:author/messages', component: () => import('@/components/tab/Messages'), props: true  },
      { path: '/user/:author/profile', component: () => import('@/components/tab/Profile')}
    ]
  },
  { path: '/user/:author/writepost', name: 'writepost', component: () => import('@/views/WritePost')},
  { path: '/user/register', component: () => import('@/views/Register')},
  { path: '/post/:postid/single', name: 'single', component: () => import('@/components/helper/Single'),props: true},
  { path: '/activity', component: () => import('@/views/Activity')},
  { path: '*', component: () => import('@/components/helper/NotFound')}
]
