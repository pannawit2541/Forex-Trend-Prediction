<script>
import { Line } from "vue-chartjs";
import { api } from "../../api";

export default {
  extends: Line,
  data() {
    return {
      date: null,
      sma_predict: null,
      sma_ture: null,
    };
  },
  methods: {

    async SMA_predict() {
      try {
        const res = (await api.get("/EURUSD/evaluate")).data;
        this.sma_predict = res.SMA_predict;
        this.date = res.Date


      } catch (error) {
        console.log(error);
      }
    },
  },

  async mounted() {
    await this.SMA_predict()
    console.log(this.sma_predict)
    this.renderChart(
      {
        labels: this.date,
        datasets: [
          {
            label: "SMA_predict",
            data: this.sma_predict,
            backgroundColor: "transparent",
            borderColor: "#63dbff",
            pointBackgroundColor: "#63dbff",
            lineTension: 0.4,
          },
          // {
          //   label: "SMA_true",
          //   data: [4, 12, 3, 7, 1, 5],
          //   backgroundColor: "transparent",
          //   borderColor: "#ffa8c4",
          //   pointBackgroundColor: "#ffa8c4",
          //   lineTension: 0.4,
          //   spanGaps: true,
          // },
        ],
      },
      {
        responsive: true,
        maintainAspectRatio: false,
        legend: {
          position: "bottom",
          align: "start",
        },
      }
    );
  },

  
};
</script>
