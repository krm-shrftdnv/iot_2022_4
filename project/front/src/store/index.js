import {createStore} from "vuex";

const state = () => ({
    co2: 1000,
    tvoc: 9
})

const mutations = {
    SET_CO2: (state, x) => state.co2 = x,
    SET_TVOC: (state, x) => state.tvoc = x,
}

const getters = {
    co2: state => state.co2,
    tvoc: state => state.tvoc
}

export default createStore({
    state: state,
    getters: getters,
    mutations: mutations
})