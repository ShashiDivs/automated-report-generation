from research_and_analyst.utils.model_loader import ModelLoader

model_loader=ModelLoader()
llm=model_loader.load_llm()
print(llm.invoke("hi").content)
