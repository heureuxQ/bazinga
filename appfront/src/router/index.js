import Vue from 'vue'
import Router from 'vue-router'
import User from '@/components/User'
import ServiceRecord from '@/components/ServiceRecord'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'User',
      component: User
    },
    {
      path: '/record',
      name: 'ServiceRecord',
      component: ServiceRecord
    }
  ]
})
