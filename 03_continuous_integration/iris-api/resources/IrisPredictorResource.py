import pickle
import sklearn
from sklearn.neighbors import KNeighborsClassifier
import json
import numpy as np
import falcon



def predict_knn(features, model):

    """
    This function gets the features and models and predicts the output
    Args:
        features(list): list of features. It must include 4 floating numbers
        model(sklearn model): knn sklearn model, loaded from models folder
    output:    
        prediceted_class(str)
    """
    
    classes = ['setosa', 'versicolor', 'virginica']
    """
    TODO: 
    predict the class!
    """
    return predicted_class

### resource
class IrisPredictorResource():
    """
    TODO: Documentation
    """
    def __init__(self, model_path, logger):
        """
        TODO: Documentation
        """
        self.logger = logger
        self.model = pickle.load(open(model_path, 'rb'))
        self.logger.info("Starting: IrisPredictor")
    
    def on_post(self, req, resp):
        """
        TODO: Documentation
        """
        try:
            self.logger.info("IrisPredictor: reading file")
            request_bytes = req.stream.read()

            try:
                request = json.loads(request_bytes.decode("utf-8"))
            
            except Exception as e:
                self.logger.error(e, exc_info=True)
                resp.status = falcon.HTTP_400
                resp.body = "Invalid JSON\n"
                return
            """
            @TODO: 
            check the quality of the input file.
            In case the quality of the input is not valid, 
            send back the correct resp.body and resp.status
            """

            ## In this part, you consider the input is correct and 
            ## just need to return the result
            prediction = predict_knn(features, self.model)

            self.logger.info('IrisPredictor: the prediction is %s' % prediction)
            response = {"predicted_class": prediction}

            self.logger.info('IrisPredictor: Sending the results \n')
            
            """
            TODO: use the correct HTTP status code
            """
            resp.status = ## FILL HERE! ##
            resp.body = json.dumps(response) + '\n'

        except Exception as e:
            self.logger.error(e, exc_info=True)
            resp.status = falcon.HTTP_500