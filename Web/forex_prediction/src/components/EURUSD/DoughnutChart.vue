<script>
import { Doughnut } from "vue-chartjs";


export default {
  extends: Doughnut,
  mounted() {
    this.renderChart(
      {
        labels :[
          "Up trend",
          "Down trend"
        ],
        datasets: [
          {
            backgroundColor: ["#55D8FB","transparent"],
            data: [40,20],
          }
        ]
      },
      { 
        responsive: true, 
        maintainAspectRatio: false ,
        
      }
    );
  }
};
</script>