#
# This is a Shiny web application. You can run the application by clicking
# the 'Run App' button above.
#
# Find out more about building applications with Shiny here:
#
#    https://shiny.posit.co/
#

library(shiny)
library(bslib)
library(ggdist)
library(distributional)
library(tidyverse)
source("vis.R")

# Define UI for application that draws a histogram
ui <- page_sidebar(

    # Application title
    title = "Visualising distributions",

    # Sidebar with a slider input for number of bins 
    sidebar = sidebar("Settings", 
                      position = "left",
                      selectInput(
                        "distribution",
                        "Select distribution",
                        choices = list(
                          "Beta" = 1,
                          "Gamma" = 2,
                          "Log-Normal" = 3
                        ),
                        selected = 1
                      ),
                      sliderInput(
                        "var1",
                        "Scale",
                        value = 5,
                        min = 1,
                        max = 10,
                        step = 0.5
                      ),
                      sliderInput(
                        "var2",
                        "Shape",
                        value = 5,
                        min = 1,
                        max = 10,
                        step = 0.5
                      )),
    card(
      textOutput("selected_distribution"),
      plotOutput("dist")
      )
)

# Define server logic required to draw a histogram
server <- function(input, output) {

    observeEvent(input$distribution, {
      if(input$distribution == 1) {
        updateSliderInput(inputId = "var1", label = "shape")
        updateSliderInput(inputId = "var2", label = "scale")
      } else
      if(input$distribution == 2) {
        updateSliderInput(inputId = "var1", label = "shape")
        updateSliderInput(inputId = "var2", label = "rate")
      } else
      if(input$distribution == 3) {
        updateSliderInput(inputId = "var1", label = "mu", min = 0, max = 7, step = 0.5)
        updateSliderInput(inputId = "var2", label = "sigma", min = 0.1, max = 1, step = 0.1)
      }
    })
    output$selected_distribution <- renderText({
      distrib <- case_when(
        input$distribution == 1 ~ "Beta",
        input$distribution == 2 ~ "Gamma",
        input$distribution == 3 ~ "Normal"
      )
      paste0("Drawing distribution ", distrib, "(", input$var1, ",", input$var2, ")")
    })
    output$dist <- renderPlot({
      dist_plot(input$distribution, input$var1, input$var2)
    })
}

# Run the application 
shinyApp(ui = ui, server = server)
