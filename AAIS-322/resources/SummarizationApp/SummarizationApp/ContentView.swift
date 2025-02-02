//
//  ContentView.swift
//  SummarizationApp
//
//  Created by Mohammad Azam on 8/20/24.
//

import SwiftUI
import SwiftSummarize


struct ContentView: View {
    
    let input = """
    In a quiet village nestled between rolling hills, an ancient oak tree stood at the heart of the town square. The tree, with its gnarled branches and lush green canopy, had witnessed countless stories over the centuries. Children played in its shade, lovers carved initials into its bark, and elders shared tales of old beneath its boughs. As the seasons changed, so did the tree, with vibrant autumn leaves giving way to the crisp whites of winter snow. Each leaf that fell seemed to carry a piece of the village's history, whispering secrets to those who would listen. In this serene setting, time seemed to slow, allowing the village's inhabitants to reflect on the beauty of nature and the passage of time.
    """
    
    var body: some View {
        VStack(alignment: .leading) {
            Text("Original Text")
                .font(.largeTitle)
                .padding([.bottom], 5)
                .fixedSize()
            
            Text(input)
                .padding([.bottom], 20)
            
            Text("Summarize Text")
                .font(.largeTitle)
                .padding([.bottom], 5)
                    
            Text(input.summarize(numberOfSentences: 1).description)
                
        }
        .padding()
    }
}

#Preview {
    ContentView()
        .frame(maxWidth: 500, maxHeight: 500)
}
