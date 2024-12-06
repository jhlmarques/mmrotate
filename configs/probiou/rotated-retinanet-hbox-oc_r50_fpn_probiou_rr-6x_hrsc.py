_base_ = '../rotated_retinanet/rotated-retinanet-hbox-oc_r50_fpn_rr-6x_hrsc.py'

model = dict(
    bbox_head=dict(
        reg_decoded_bbox=True,
        loss_bbox=dict(
            _delete_=True, type='GDLoss', loss_type='probiou',
            loss_weight=1.0)))
