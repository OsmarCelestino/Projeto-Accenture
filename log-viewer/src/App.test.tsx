import React from 'react';
import { render, screen } from '@testing-library/react';
import LogTable from './LogTable';

describe('LogTable component', () => {
    test('renders LogTable component', () => {
        render(<LogTable />);
        expect(screen.getByText('Filtrar')).toBeInTheDocument();
        expect(screen.getByText('Processar Logs')).toBeInTheDocument();
        expect(screen.getByLabelText('Data Início')).toBeInTheDocument();
        expect(screen.getByLabelText('Data Fim')).toBeInTheDocument();
    });
});
