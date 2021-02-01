<script>
import { Bar } from "vue-chartjs";

export default {
  extends: Bar,
 
  mounted() {
    this.renderChart(
      {
        labels: [
          "January",
          "February",
          "March",
          "April",
          "May",
          "June",
        ],
        datasets: [
          {
            label: "2020",
            backgroundColor: "#55D8FB",
            data: [40, 20, 12, 39, 15,41],
            barThickness : 8,
            barPercentage: 0.5
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
