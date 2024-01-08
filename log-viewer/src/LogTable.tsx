import React, { useState } from 'react';
import axios from 'axios';
import { DatePicker, LocalizationProvider } from '@mui/x-date-pickers';
import { AdapterDateFns } from '@mui/x-date-pickers/AdapterDateFns';
import { CircularProgress, TextField, Button, Container, Paper, Box, Grid, Table, TableBody, TableCell, TableContainer, TableHead, TableRow, TablePagination } from '@mui/material';
import SearchIcon from '@mui/icons-material/Search';
import ClearIcon from '@mui/icons-material/Clear';

interface Log {
  _id: string;
  ip: string;
  date: string;
  activity_description: string;
  additional_message: string;
}

function LogTable(): JSX.Element {
  const [logs, setLogs] = useState<Log[]>([]);
  const [isLoading, setIsLoading] = useState(false);
  const [startDate, setStartDate] = useState<Date | null>(null);
  const [endDate, setEndDate] = useState<Date | null>(null);
  const [messageFilter, setMessageFilter] = useState("");
  const [page, setPage] = useState(0);
  const [rowsPerPage, setRowsPerPage] = useState(20);

  const fetchFilteredLogs = () => {
    setIsLoading(true);
    const params = {
        start_date: (startDate instanceof Date && !isNaN(startDate.getTime())) ? startDate.toISOString() : "",
        end_date: (endDate instanceof Date && !isNaN(endDate.getTime())) ? endDate.toISOString() : "",
        message_contains: messageFilter,
    };

    axios
      .post("http://localhost:8000/logs/get/", params)
      .then((response) => {
        setLogs(response.data);
        setIsLoading(false);
      })
      .catch((error) => {
        console.error("Error fetching data: ", error);
        setIsLoading(false);
      });
  };

  const processLogs = () => {
    axios
      .post("http://localhost:8000/logs/process-logs/")
      .then((response) => alert("Logs processed: " + response.data.message))
      .catch((error) => console.error("Error processing logs: ", error));
  };

  const handleClearFilters = () => {
    setStartDate(null);
    setEndDate(null);
    setMessageFilter('');
    setLogs([]);
  };

  const handleChangePage = (event: unknown, newPage: number) => {
    setPage(newPage);
  };

  const handleChangeRowsPerPage = (event: React.ChangeEvent<HTMLInputElement>) => {
    setRowsPerPage(parseInt(event.target.value, 10));
    setPage(0);
  };

  return (
    <LocalizationProvider dateAdapter={AdapterDateFns}>
      <Container   sx={{ mt: 4, mb: 4,  width:'2000px' }}>
        <Paper sx={{ p: 2, display: 'flex', flexDirection: 'column', background: '#f5f5f5' }}>
          <Grid container spacing={2} alignItems="center">
            <Grid item xs={3}>
              <DatePicker
                label="Data Início"
                value={startDate}
                onChange={setStartDate}
              />
            </Grid>
            <Grid item xs={3}>
              <DatePicker
                label="Data Fim"
                value={endDate}
                onChange={setEndDate}
              />
            </Grid>
            <Grid item xs={3}>
              <TextField
                label="Filtrar Mensagem"
                variant="outlined"
                fullWidth
                value={messageFilter}
                onChange={(e) => setMessageFilter(e.target.value)}
              />
            </Grid>
            <Grid item spacing={2} xs={3}>
              <Button startIcon={<SearchIcon />} variant="contained" color="primary" onClick={fetchFilteredLogs} style={{ marginRight: '8px' }}>
                Filtrar
              </Button>
              <Button startIcon={<ClearIcon />} variant="outlined" color="primary" onClick={handleClearFilters}>
                Limpar
              </Button>
             
            </Grid>
            <Grid item xs={3}>
              <Button  color="secondary" variant="contained" onClick={processLogs} style={{ marginBottom: '10px' }}>
                Processar Logs
              </Button>
            </Grid>
          </Grid>
          
          {isLoading ? (
            <Box sx={{ display: 'flex', justifyContent: 'center', p: 3 }}>
              <CircularProgress />
            </Box>
          ) : logs.length > 0 && (
            <TableContainer component={Paper}>                
              <Table aria-label="simple table">
                <TableHead>
                  <TableRow>
                    <TableCell>IP</TableCell>
                    <TableCell sx={{ minWidth: '150px' }} align="right">Data</TableCell>
                    <TableCell align="right">Descrição da Atividade</TableCell>
                    <TableCell align="right" sx={{ minWidth: '200px' }}>Mensagem Adicional</TableCell>
                  </TableRow>
                </TableHead>
                <TableBody>
                  {logs.slice(page * rowsPerPage, page * rowsPerPage + rowsPerPage).map((log) => (
                    <TableRow key={log._id}>
                      <TableCell component="th" scope="row">{log.ip}</TableCell>
                      <TableCell align="right" sx={{ minWidth: '150px' }}>{new Date(log.date).toLocaleString()}</TableCell>
                      <TableCell align="right">{log.activity_description}</TableCell>
                      <TableCell align="right" sx={{ minWidth: '200px' }}>{log.additional_message}</TableCell>
                    </TableRow>
                  ))}
                </TableBody>
              </Table>
              <TablePagination
                component="div"
                count={logs.length}
                page={page}
                onPageChange={handleChangePage}
                rowsPerPage={rowsPerPage}
                onRowsPerPageChange={handleChangeRowsPerPage}
              />
            </TableContainer>
          )}

    
        </Paper>
      </Container>
    </LocalizationProvider>
  );
}

export default LogTable;
