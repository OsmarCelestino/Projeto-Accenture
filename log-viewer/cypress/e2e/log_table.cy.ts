/// <reference types="cypress" />

describe('LogTable', () => {
  beforeEach(() => {
    cy.visit('http://localhost:3000');
  });

  it('permite ao usuário filtrar', () => {
   
    cy.contains('Data Início').parent().find('input').type('01-01-2022');
    cy.contains('Data Fim').parent().find('input').type('03-01-2023');
    

    cy.get('#filtrarTeste').type('Congue');

    cy.get('#filtrarButton').click();


    cy.get('table').should('be.visible');
    

    cy.get('table tbody tr').should('have.length.at.least', 1);

    cy.get('#limparButton').click();
    cy.get('table tbody tr').should('not.exist');
  });
});
