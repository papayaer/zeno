
import { isValidJwt } from '@/utils'

export default {
  isAuthenticated(state) {
    return isValidJwt(state.jwt)
  },
  expToken() {
    const token = localStorage.getItem('token')
    return isValidJwt(token) ? true : false
  }
}
