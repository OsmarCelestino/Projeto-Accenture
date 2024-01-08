import React from 'react';
import LogTable from './LogTable';
import Container from '@mui/material/Container';

function App(): JSX.Element {
  return (
    <Container>
      <h1>Visualizador de Logs</h1>
      <LogTable />
    </Container>
  );
}

export default App;
