<script>
import { Line } from "vue-chartjs";
import { api } from "../../api";

export default {
  extends: Line,
  data() {
    return {
      date: [],
      sma_predict: [],
      sma_true: [],
    };
  },
  methods: {
    async SMA_predict() {
      try {
        const res = (await api.get("/EURUSD/evaluate")).data;
        const len_date = res.Date.length;
        const len_pre = res.SMA_predict.length;
        const len_true = res.SMA_true.length;
        // this.sma_predict = res.SMA_predict;
        // this.sma_true = res.SMA_true;
        // this.date = res.Date;
        for (let i = 6; i > 0; i--) {
          this.sma_predict.push(res.SMA_predict[len_pre - 24 * i]);
          this.date.push(res.Date[len_date - 24 * i]);
          if (i == 1) {
            this.sma_true.push(null);
          } else {
            this.sma_true.push(res.SMA_true[len_true - 24 * i]);
          }
        }
      } catch (error) {
        console.log(error);
      }
    },
  },

  async mounted() {
    await this.SMA_predict();
    this.renderChart(
      {
        labels: this.date,
        datasets: [
          {
            label: "SMA_predict",
            data: this.sma_predict,
            backgroundColor: "#63dbff",
            borderColor: "#63dbff",
            borderWidth: 3,
            fill: false,
            pointRadius : 0,
          },
          {
            label: "SMA_true",
            data: this.sma_true,
            backgroundColor: "transparent",
            borderColor: "#ffa8c4",
            pointBackgroundColor: "#ffa8c4",
            fill: false,
            pointRadius : 0,
          },
        ],
      },
      {
        responsive: true,
        maintainAspectRatio: false,
        legend: {
          position: "bottom",
          align: "start",
          
          labels:{
            fontColor: "rgba(77, 79, 92, 0.5)",
            boxWidth : 30
          }
        },
        scales: {
          
          xAxes: [
            {
              
              gridLines: {
                display: false,
              },
              ticks: {
                fontColor: "#7C828A",
                 padding : 25,
              },
            },
          ],
          yAxes: [
            {
              gridLines: {
                display: true,
                color: "rgba(77, 79, 92, 0.1)",
                drawBorder : false
              },
              ticks: {
                padding : 25,
                fontColor: "#7C828A",
                maxTicksLimit : 6
              },
            },
          ],
        },
      }
    );
  },
};
</script>
