import React from 'react';
import './App.css';
import { MovieListContainer } from './components/MovieList';
import { Container } from 'react-bootstrap';

const App: React.FC = () => {
  return (
  <Container>
  <MovieListContainer />
  </Container>
  );
}

export default App;
