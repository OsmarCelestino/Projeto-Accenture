/// <reference types="cypress" />

describe('LogTable', () => {
    beforeEach(() => {
      cy.visit('http://localhost:3000');
    });
  
    it('permite ao usuário filtrar', () => {
     
      cy.contains('Data Início').parent().find('input').type('2022-01-01');
      cy.contains('Data Fim').parent().find('input').type('2022-01-31');
      

      cy.contains('Filtrar Mensagem').parent().find('input').type('Erro');

      cy.contains('FILTRAR').click();
  

      cy.get('table').should('be.visible');
      
  
      cy.get('table tbody tr').should('have.length.at.least', 1);

      cy.contains('LIMPAR').click();
      cy.get('table tbody tr').should('not.exist');
    });
  });
  