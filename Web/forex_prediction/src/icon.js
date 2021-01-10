import Vue from 'vue'
import { library } from '@fortawesome/fontawesome-svg-core'
import { faArrowUp,faArrowDown } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon} from '@fortawesome/vue-fontawesome'


library.add(faArrowUp,faArrowDown)
Vue.component('fa-icon',FontAwesomeIcon)
