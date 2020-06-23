from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
from detectron2.utils.visualizer import Visualizer
from detectron2.data import MetadataCatalog
import cv2


def detect(img1):
    # load image
    img = cv2.imread(img1)

    # set config
    cfg = get_cfg()
    cfg.merge_from_file("detectron2/configs/COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml")
    cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.5
    cfg.MODEL.WEIGHTS = "detectron2/model/model_final_f10217.pkl"

    # predict
    predictor = DefaultPredictor(cfg)
    outputs = predictor(img)

    # visualization
    v = Visualizer(img[:,:,::-1], MetadataCatalog.get(cfg.DATASETS.TRAIN[0]), scale=1.2)
    v = v.draw_instance_predictions(outputs["instances"].to("cpu"))

    return v.get_image()[:,:,::-1]


    # cv2.imwrite('output.jpg',v.get_image()[:,:,::-1])