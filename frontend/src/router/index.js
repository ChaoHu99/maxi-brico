import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/sign-up',
    name: 'SignUp',
    component: () => import('../views/SignUp.vue')
  },
  {
    path: '/product/:barcode',
    name: 'Products',
    component: () => import('../views/Products.vue'),
    meta: {
      requiresLogin: true
    }
  },
  {
    path: '/cart',
    name: 'Cart',
    component: () => import('../components/Cart.vue'),
    meta: {
      requiresLogin: true
    }
  },
  {
    path: '/payment-success',
    name: 'PaymentSuccess',
    component: () => import('../views/PaymentSuccess.vue')
  },
  {
    path: '/payment-failed',
    name: 'PaymentFailed',
    component: () => import('../views/PaymentFailed.vue')
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import('../views/Login.vue')
  },
  {
    path: '/logout',
    name: 'Logout',
    component: () => import('../views/Logout.vue')
  },
  {
    path: '/terms',
    name: 'TermsConditions',
    component: () => import('../views/TermsConditions.vue')
  },
  {
    path: '/my-orders',
    name: 'MyOrders',
    component: () => import('../views/MyOrders.vue'),
    meta: {
      requiresLogin: true
    }
  },
]

const router = new VueRouter({
  routes,
  mode:'history'
})

export default router
