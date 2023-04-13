import './App.css';
import RecommendationForm from './components/RecommendationForm';

function App() {
  console.log("rendering App")
  return (
    <div className="App">
      <h1>Steam Game Recommendation Engine</h1>
      <RecommendationForm />
    </div>
  );
}

export default App;
