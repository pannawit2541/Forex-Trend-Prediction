import Vue from 'vue'
import { library } from '@fortawesome/fontawesome-svg-core'
import { faArrowUp,faArrowDown,faChartBar,faCoins,faChartPie,faEuroSign,faYenSign,faPoundSign } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon} from '@fortawesome/vue-fontawesome'


library.add(faArrowUp,faArrowDown,faChartBar,faCoins,faChartPie,faEuroSign,faYenSign,faPoundSign)
Vue.component('fa-icon',FontAwesomeIcon)
