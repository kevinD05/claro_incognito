Feature: Validamos ingresar a la pagina web y rellenar formulario

@claro
Scenario: validamos rellenar formulario
    Given Ingresamos a la url "claro_url"
    When Aceptamos las cookies
    And Damos click en el boton solutions y ingresamos a MPLS
    And Rellenaremos el formulario
    And daremos click en el boton submit
    Then validamos mensaje de error