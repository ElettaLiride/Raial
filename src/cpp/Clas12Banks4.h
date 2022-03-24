//// File automatically produced by create_hiponodes.py do not make changes here!!
#include "reader.h"





/*************************************************************************/
/*  Declaration of bank variables */
/*************************************************************************/
hipo::bank *MC__Header ;
int get_MC__Header(int row);
int  MC__Header_run ;
int  MC__Header_event ;
short  MC__Header_type ;
float  MC__Header_helicity ;
hipo::bank *RAW__scaler ;
int get_RAW__scaler(int row);
short  RAW__scaler_crate ;
short  RAW__scaler_slot ;
short  RAW__scaler_channel ;
short  RAW__scaler_helicity ;
short  RAW__scaler_quartet ;
long  RAW__scaler_value ;
hipo::bank *HEL__online ;
int get_HEL__online(int row);
short  HEL__online_helicity ;
short  HEL__online_helicityRaw ;
hipo::bank *REC__Event ;
int get_REC__Event(int row);
long  REC__Event_category ;
long  REC__Event_topology ;
float  REC__Event_beamCharge ;
double  REC__Event_liveTime ;
float  REC__Event_startTime ;
float  REC__Event_RFTime ;
short  REC__Event_helicity ;
short  REC__Event_helicityRaw ;
float  REC__Event_procTime ;
hipo::bank *REC__Particle ;
int get_REC__Particle(int row);
int  REC__Particle_pid ;
float  REC__Particle_px ;
float  REC__Particle_py ;
float  REC__Particle_pz ;
float  REC__Particle_vx ;
float  REC__Particle_vy ;
float  REC__Particle_vz ;
float  REC__Particle_vt ;
short  REC__Particle_charge ;
float  REC__Particle_beta ;
float  REC__Particle_chi2pid ;
short  REC__Particle_status ;
hipo::bank *RUN__config ;
int get_RUN__config(int row);
int  RUN__config_run ;
int  RUN__config_event ;
int  RUN__config_unixtime ;
long  RUN__config_trigger ;
long  RUN__config_timestamp ;
short  RUN__config_type ;
short  RUN__config_mode ;
float  RUN__config_torus ;
float  RUN__config_solenoid ;
hipo::bank *REC__Traj ;
int get_REC__Traj(int row);
short  REC__Traj_pindex ;
short  REC__Traj_index ;
short  REC__Traj_detector ;
short  REC__Traj_layer ;
float  REC__Traj_x ;
float  REC__Traj_y ;
float  REC__Traj_z ;
float  REC__Traj_cx ;
float  REC__Traj_cy ;
float  REC__Traj_cz ;
float  REC__Traj_path ;
hipo::bank *RICH__hits ;
int get_RICH__hits(int row);
short  RICH__hits_id ;
short  RICH__hits_sector ;
short  RICH__hits_tile ;
short  RICH__hits_pmt ;
short  RICH__hits_anode ;
float  RICH__hits_x ;
float  RICH__hits_y ;
float  RICH__hits_z ;
float  RICH__hits_time ;
float  RICH__hits_rawtime ;
short  RICH__hits_cluster ;
short  RICH__hits_xtalk ;
short  RICH__hits_duration ;
hipo::bank *MC__True ;
int get_MC__True(int row);
short  MC__True_detector ;
int  MC__True_pid ;
int  MC__True_mpid ;
int  MC__True_tid ;
int  MC__True_mtid ;
int  MC__True_otid ;
float  MC__True_trackE ;
float  MC__True_totEdep ;
float  MC__True_avgX ;
float  MC__True_avgY ;
float  MC__True_avgZ ;
float  MC__True_avgLx ;
float  MC__True_avgLy ;
float  MC__True_avgLz ;
float  MC__True_px ;
float  MC__True_py ;
float  MC__True_pz ;
float  MC__True_vx ;
float  MC__True_vy ;
float  MC__True_vz ;
float  MC__True_mvx ;
float  MC__True_mvy ;
float  MC__True_mvz ;
float  MC__True_avgT ;
int  MC__True_nsteps ;
int  MC__True_procID ;
int  MC__True_hitn ;
hipo::bank *REC__Calorimeter ;
int get_REC__Calorimeter(int row);
short  REC__Calorimeter_index ;
short  REC__Calorimeter_pindex ;
short  REC__Calorimeter_detector ;
short  REC__Calorimeter_sector ;
short  REC__Calorimeter_layer ;
float  REC__Calorimeter_energy ;
float  REC__Calorimeter_time ;
float  REC__Calorimeter_path ;
float  REC__Calorimeter_chi2 ;
float  REC__Calorimeter_x ;
float  REC__Calorimeter_y ;
float  REC__Calorimeter_z ;
float  REC__Calorimeter_hx ;
float  REC__Calorimeter_hy ;
float  REC__Calorimeter_hz ;
float  REC__Calorimeter_lu ;
float  REC__Calorimeter_lv ;
float  REC__Calorimeter_lw ;
float  REC__Calorimeter_du ;
float  REC__Calorimeter_dv ;
float  REC__Calorimeter_dw ;
float  REC__Calorimeter_m2u ;
float  REC__Calorimeter_m2v ;
float  REC__Calorimeter_m2w ;
float  REC__Calorimeter_m3u ;
float  REC__Calorimeter_m3v ;
float  REC__Calorimeter_m3w ;
short  REC__Calorimeter_status ;
hipo::bank *REC__CovMat ;
int get_REC__CovMat(int row);
short  REC__CovMat_index ;
short  REC__CovMat_pindex ;
float  REC__CovMat_C11 ;
float  REC__CovMat_C12 ;
float  REC__CovMat_C13 ;
float  REC__CovMat_C14 ;
float  REC__CovMat_C15 ;
float  REC__CovMat_C22 ;
float  REC__CovMat_C23 ;
float  REC__CovMat_C24 ;
float  REC__CovMat_C25 ;
float  REC__CovMat_C33 ;
float  REC__CovMat_C34 ;
float  REC__CovMat_C35 ;
float  REC__CovMat_C44 ;
float  REC__CovMat_C45 ;
float  REC__CovMat_C55 ;
hipo::bank *RICH__response ;
int get_RICH__response(int row);
short  RICH__response_index ;
short  RICH__response_pindex ;
short  RICH__response_detector ;
short  RICH__response_sector ;
short  RICH__response_layer ;
float  RICH__response_energy ;
float  RICH__response_time ;
float  RICH__response_path ;
float  RICH__response_chi2 ;
float  RICH__response_x ;
float  RICH__response_y ;
float  RICH__response_z ;
float  RICH__response_hx ;
float  RICH__response_hy ;
float  RICH__response_hz ;
short  RICH__response_status ;
hipo::bank *MC__Event ;
int get_MC__Event(int row);
short  MC__Event_npart ;
short  MC__Event_atarget ;
short  MC__Event_ztarget ;
float  MC__Event_ptarget ;
float  MC__Event_pbeam ;
short  MC__Event_btype ;
float  MC__Event_ebeam ;
short  MC__Event_targetid ;
short  MC__Event_processid ;
float  MC__Event_weight ;
hipo::bank *RAW__epics ;
int get_RAW__epics(int row);
short  RAW__epics_json ;
hipo::bank *RICH__clusters ;
int get_RICH__clusters(int row);
short  RICH__clusters_id ;
short  RICH__clusters_size ;
short  RICH__clusters_sector ;
short  RICH__clusters_tile ;
short  RICH__clusters_pmt ;
float  RICH__clusters_charge ;
float  RICH__clusters_time ;
float  RICH__clusters_rawtime ;
float  RICH__clusters_x ;
float  RICH__clusters_y ;
float  RICH__clusters_z ;
float  RICH__clusters_wtime ;
float  RICH__clusters_wx ;
float  RICH__clusters_wy ;
float  RICH__clusters_wz ;
hipo::bank *REC__Scintillator ;
int get_REC__Scintillator(int row);
short  REC__Scintillator_index ;
short  REC__Scintillator_pindex ;
short  REC__Scintillator_detector ;
short  REC__Scintillator_sector ;
short  REC__Scintillator_layer ;
short  REC__Scintillator_component ;
float  REC__Scintillator_energy ;
float  REC__Scintillator_time ;
float  REC__Scintillator_path ;
float  REC__Scintillator_chi2 ;
float  REC__Scintillator_x ;
float  REC__Scintillator_y ;
float  REC__Scintillator_z ;
float  REC__Scintillator_hx ;
float  REC__Scintillator_hy ;
float  REC__Scintillator_hz ;
short  REC__Scintillator_status ;
float  REC__Scintillator_dedx ;
hipo::bank *MC__Particle ;
int get_MC__Particle(int row);
int  MC__Particle_pid ;
float  MC__Particle_px ;
float  MC__Particle_py ;
float  MC__Particle_pz ;
float  MC__Particle_vx ;
float  MC__Particle_vy ;
float  MC__Particle_vz ;
float  MC__Particle_vt ;
hipo::bank *RICH__tdc ;
int get_RICH__tdc(int row);
short  RICH__tdc_sector ;
short  RICH__tdc_layer ;
short  RICH__tdc_component ;
short  RICH__tdc_order ;
int  RICH__tdc_TDC ;
hipo::bank *RUN__scaler ;
int get_RUN__scaler(int row);
float  RUN__scaler_fcupgated ;
float  RUN__scaler_fcup ;
float  RUN__scaler_livetime ;
hipo::bank *RICH__hadrons ;
int get_RICH__hadrons(int row);
short  RICH__hadrons_id ;
short  RICH__hadrons_hit_index ;
short  RICH__hadrons_particle_index ;
float  RICH__hadrons_traced_the ;
float  RICH__hadrons_traced_phi ;
float  RICH__hadrons_traced_hitx ;
float  RICH__hadrons_traced_hity ;
float  RICH__hadrons_traced_hitz ;
float  RICH__hadrons_traced_time ;
float  RICH__hadrons_traced_path ;
short  RICH__hadrons_traced_ilay ;
short  RICH__hadrons_traced_ico ;
float  RICH__hadrons_traced_emix ;
float  RICH__hadrons_traced_emiy ;
float  RICH__hadrons_traced_emiz ;
float  RICH__hadrons_EtaC_ele ;
float  RICH__hadrons_EtaC_pi ;
float  RICH__hadrons_EtaC_k ;
float  RICH__hadrons_EtaC_pr ;
float  RICH__hadrons_EtaC_min ;
float  RICH__hadrons_EtaC_max ;
hipo::bank *REC__Track ;
int get_REC__Track(int row);
short  REC__Track_index ;
short  REC__Track_pindex ;
short  REC__Track_detector ;
short  REC__Track_sector ;
short  REC__Track_status ;
short  REC__Track_q ;
float  REC__Track_chi2 ;
short  REC__Track_NDF ;
hipo::bank *RICH__ringCher ;
int get_RICH__ringCher(int row);
short  RICH__ringCher_id ;
short  RICH__ringCher_hindex ;
short  RICH__ringCher_pindex ;
short  RICH__ringCher_pmt ;
short  RICH__ringCher_anode ;
float  RICH__ringCher_time ;
float  RICH__ringCher_apath ;
float  RICH__ringCher_atime ;
float  RICH__ringCher_aEtaC ;
float  RICH__ringCher_tpath ;
float  RICH__ringCher_ttime ;
float  RICH__ringCher_tEtaC ;
short  RICH__ringCher_nrfl ;
short  RICH__ringCher_1rfl ;
hipo::bank *REC__ForwardTagger ;
int get_REC__ForwardTagger(int row);
short  REC__ForwardTagger_index ;
short  REC__ForwardTagger_pindex ;
short  REC__ForwardTagger_detector ;
short  REC__ForwardTagger_layer ;
float  REC__ForwardTagger_energy ;
float  REC__ForwardTagger_time ;
float  REC__ForwardTagger_path ;
float  REC__ForwardTagger_chi2 ;
float  REC__ForwardTagger_x ;
float  REC__ForwardTagger_y ;
float  REC__ForwardTagger_z ;
float  REC__ForwardTagger_dx ;
float  REC__ForwardTagger_dy ;
float  REC__ForwardTagger_radius ;
short  REC__ForwardTagger_size ;
short  REC__ForwardTagger_status ;
hipo::bank *RICH__hadCher ;
int get_RICH__hadCher(int row);
short  RICH__hadCher_id ;
short  RICH__hadCher_hindex ;
short  RICH__hadCher_pindex ;
short  RICH__hadCher_emilay ;
short  RICH__hadCher_emico ;
short  RICH__hadCher_enico ;
short  RICH__hadCher_emqua ;
float  RICH__hadCher_mchi2 ;
float  RICH__hadCher_ch_min ;
float  RICH__hadCher_ch_max ;
float  RICH__hadCher_dt_max ;
float  RICH__hadCher_ch_dir ;
float  RICH__hadCher_ch_lat ;
float  RICH__hadCher_ch_spe ;
short  RICH__hadCher_best_PID ;
float  RICH__hadCher_RQ_prob ;
float  RICH__hadCher_el_prob ;
float  RICH__hadCher_pi_prob ;
float  RICH__hadCher_k_prob ;
float  RICH__hadCher_pr_prob ;
hipo::bank *REC__Cherenkov ;
int get_REC__Cherenkov(int row);
short  REC__Cherenkov_index ;
short  REC__Cherenkov_pindex ;
short  REC__Cherenkov_detector ;
short  REC__Cherenkov_sector ;
float  REC__Cherenkov_nphe ;
float  REC__Cherenkov_time ;
float  REC__Cherenkov_path ;
float  REC__Cherenkov_chi2 ;
float  REC__Cherenkov_x ;
float  REC__Cherenkov_y ;
float  REC__Cherenkov_z ;
float  REC__Cherenkov_dtheta ;
float  REC__Cherenkov_dphi ;
short  REC__Cherenkov_status ;
hipo::bank *RICH__photons ;
int get_RICH__photons(int row);
short  RICH__photons_id ;
short  RICH__photons_type ;
short  RICH__photons_hit_index ;
short  RICH__photons_hadron_index ;
float  RICH__photons_start_time ;
float  RICH__photons_analytic_the ;
float  RICH__photons_analytic_phi ;
float  RICH__photons_analytic_path ;
float  RICH__photons_analytic_time ;
float  RICH__photons_analytic_EtaC ;
float  RICH__photons_analytic_aeron ;
float  RICH__photons_analytic_elpr ;
float  RICH__photons_analytic_pipr ;
float  RICH__photons_analytic_kpr ;
float  RICH__photons_analytic_prpr ;
float  RICH__photons_analytic_bgpr ;
float  RICH__photons_traced_the ;
float  RICH__photons_traced_phi ;
float  RICH__photons_traced_hitx ;
float  RICH__photons_traced_hity ;
float  RICH__photons_traced_hitz ;
float  RICH__photons_traced_path ;
float  RICH__photons_traced_time ;
short  RICH__photons_traced_nrfl ;
short  RICH__photons_traced_nrfr ;
short  RICH__photons_traced_1rfl ;
float  RICH__photons_traced_EtaC ;
float  RICH__photons_traced_aeron ;
float  RICH__photons_traced_elpr ;
float  RICH__photons_traced_pipr ;
float  RICH__photons_traced_kpr ;
float  RICH__photons_traced_prpr ;
float  RICH__photons_traced_bgpr ;
hipo::bank *RECFT__Particle ;
int get_RECFT__Particle(int row);
int  RECFT__Particle_pid ;
float  RECFT__Particle_vt ;
float  RECFT__Particle_beta ;
float  RECFT__Particle_chi2pid ;
short  RECFT__Particle_status ;
hipo::bank *HEL__flip ;
int get_HEL__flip(int row);
int  HEL__flip_run ;
int  HEL__flip_event ;
long  HEL__flip_timestamp ;
short  HEL__flip_helicity ;
short  HEL__flip_helicityRaw ;
short  HEL__flip_pair ;
short  HEL__flip_pattern ;
short  HEL__flip_status ;
hipo::bank *RECFT__Event ;
int get_RECFT__Event(int row);
long  RECFT__Event_category ;
float  RECFT__Event_startTime ;
hipo::bank *MC__Lund ;
int get_MC__Lund(int row);
short  MC__Lund_index ;
float  MC__Lund_lifetime ;
short  MC__Lund_type ;
int  MC__Lund_pid ;
short  MC__Lund_parent ;
short  MC__Lund_daughter ;
float  MC__Lund_px ;
float  MC__Lund_py ;
float  MC__Lund_pz ;
float  MC__Lund_energy ;
float  MC__Lund_mass ;
float  MC__Lund_vx ;
float  MC__Lund_vy ;
float  MC__Lund_vz ;



/*************************************************************************/
/* Hipo reader objects */
/*************************************************************************/
hipo::reader *fReader;
hipo::event *fEvent;
hipo::dictionary *fFactory;





/*************************************************************************/
/* Hipo reader functions */
/*************************************************************************/
int get_MC__Header(int row){
	MC__Header_run = MC__Header->getInt("run",row);
	MC__Header_event = MC__Header->getInt("event",row);
	MC__Header_type = MC__Header->getByte("type",row);
	MC__Header_helicity = MC__Header->getFloat("helicity",row);
	return 0;
} 

int get_RAW__scaler(int row){
	RAW__scaler_crate = RAW__scaler->getByte("crate",row);
	RAW__scaler_slot = RAW__scaler->getByte("slot",row);
	RAW__scaler_channel = RAW__scaler->getShort("channel",row);
	RAW__scaler_helicity = RAW__scaler->getByte("helicity",row);
	RAW__scaler_quartet = RAW__scaler->getByte("quartet",row);
	RAW__scaler_value = RAW__scaler->getLong("value",row);
	return 0;
} 

int get_HEL__online(int row){
	HEL__online_helicity = HEL__online->getByte("helicity",row);
	HEL__online_helicityRaw = HEL__online->getByte("helicityRaw",row);
	return 0;
} 

int get_REC__Event(int row){
	REC__Event_category = REC__Event->getLong("category",row);
	REC__Event_topology = REC__Event->getLong("topology",row);
	REC__Event_beamCharge = REC__Event->getFloat("beamCharge",row);
	REC__Event_liveTime = REC__Event->getDouble("liveTime",row);
	REC__Event_startTime = REC__Event->getFloat("startTime",row);
	REC__Event_RFTime = REC__Event->getFloat("RFTime",row);
	REC__Event_helicity = REC__Event->getByte("helicity",row);
	REC__Event_helicityRaw = REC__Event->getByte("helicityRaw",row);
	REC__Event_procTime = REC__Event->getFloat("procTime",row);
	return 0;
} 

int get_REC__Particle(int row){
	REC__Particle_pid = REC__Particle->getInt("pid",row);
	REC__Particle_px = REC__Particle->getFloat("px",row);
	REC__Particle_py = REC__Particle->getFloat("py",row);
	REC__Particle_pz = REC__Particle->getFloat("pz",row);
	REC__Particle_vx = REC__Particle->getFloat("vx",row);
	REC__Particle_vy = REC__Particle->getFloat("vy",row);
	REC__Particle_vz = REC__Particle->getFloat("vz",row);
	REC__Particle_vt = REC__Particle->getFloat("vt",row);
	REC__Particle_charge = REC__Particle->getByte("charge",row);
	REC__Particle_beta = REC__Particle->getFloat("beta",row);
	REC__Particle_chi2pid = REC__Particle->getFloat("chi2pid",row);
	REC__Particle_status = REC__Particle->getShort("status",row);
	return 0;
} 

int get_RUN__config(int row){
	RUN__config_run = RUN__config->getInt("run",row);
	RUN__config_event = RUN__config->getInt("event",row);
	RUN__config_unixtime = RUN__config->getInt("unixtime",row);
	RUN__config_trigger = RUN__config->getLong("trigger",row);
	RUN__config_timestamp = RUN__config->getLong("timestamp",row);
	RUN__config_type = RUN__config->getByte("type",row);
	RUN__config_mode = RUN__config->getByte("mode",row);
	RUN__config_torus = RUN__config->getFloat("torus",row);
	RUN__config_solenoid = RUN__config->getFloat("solenoid",row);
	return 0;
} 

int get_REC__Traj(int row){
	REC__Traj_pindex = REC__Traj->getShort("pindex",row);
	REC__Traj_index = REC__Traj->getShort("index",row);
	REC__Traj_detector = REC__Traj->getByte("detector",row);
	REC__Traj_layer = REC__Traj->getByte("layer",row);
	REC__Traj_x = REC__Traj->getFloat("x",row);
	REC__Traj_y = REC__Traj->getFloat("y",row);
	REC__Traj_z = REC__Traj->getFloat("z",row);
	REC__Traj_cx = REC__Traj->getFloat("cx",row);
	REC__Traj_cy = REC__Traj->getFloat("cy",row);
	REC__Traj_cz = REC__Traj->getFloat("cz",row);
	REC__Traj_path = REC__Traj->getFloat("path",row);
	return 0;
} 

int get_RICH__hits(int row){
	RICH__hits_id = RICH__hits->getShort("id",row);
	RICH__hits_sector = RICH__hits->getShort("sector",row);
	RICH__hits_tile = RICH__hits->getShort("tile",row);
	RICH__hits_pmt = RICH__hits->getShort("pmt",row);
	RICH__hits_anode = RICH__hits->getShort("anode",row);
	RICH__hits_x = RICH__hits->getFloat("x",row);
	RICH__hits_y = RICH__hits->getFloat("y",row);
	RICH__hits_z = RICH__hits->getFloat("z",row);
	RICH__hits_time = RICH__hits->getFloat("time",row);
	RICH__hits_rawtime = RICH__hits->getFloat("rawtime",row);
	RICH__hits_cluster = RICH__hits->getShort("cluster",row);
	RICH__hits_xtalk = RICH__hits->getShort("xtalk",row);
	RICH__hits_duration = RICH__hits->getShort("duration",row);
	return 0;
} 

int get_MC__True(int row){
	MC__True_detector = MC__True->getByte("detector",row);
	MC__True_pid = MC__True->getInt("pid",row);
	MC__True_mpid = MC__True->getInt("mpid",row);
	MC__True_tid = MC__True->getInt("tid",row);
	MC__True_mtid = MC__True->getInt("mtid",row);
	MC__True_otid = MC__True->getInt("otid",row);
	MC__True_trackE = MC__True->getFloat("trackE",row);
	MC__True_totEdep = MC__True->getFloat("totEdep",row);
	MC__True_avgX = MC__True->getFloat("avgX",row);
	MC__True_avgY = MC__True->getFloat("avgY",row);
	MC__True_avgZ = MC__True->getFloat("avgZ",row);
	MC__True_avgLx = MC__True->getFloat("avgLx",row);
	MC__True_avgLy = MC__True->getFloat("avgLy",row);
	MC__True_avgLz = MC__True->getFloat("avgLz",row);
	MC__True_px = MC__True->getFloat("px",row);
	MC__True_py = MC__True->getFloat("py",row);
	MC__True_pz = MC__True->getFloat("pz",row);
	MC__True_vx = MC__True->getFloat("vx",row);
	MC__True_vy = MC__True->getFloat("vy",row);
	MC__True_vz = MC__True->getFloat("vz",row);
	MC__True_mvx = MC__True->getFloat("mvx",row);
	MC__True_mvy = MC__True->getFloat("mvy",row);
	MC__True_mvz = MC__True->getFloat("mvz",row);
	MC__True_avgT = MC__True->getFloat("avgT",row);
	MC__True_nsteps = MC__True->getInt("nsteps",row);
	MC__True_procID = MC__True->getInt("procID",row);
	MC__True_hitn = MC__True->getInt("hitn",row);
	return 0;
} 

int get_REC__Calorimeter(int row){
	REC__Calorimeter_index = REC__Calorimeter->getShort("index",row);
	REC__Calorimeter_pindex = REC__Calorimeter->getShort("pindex",row);
	REC__Calorimeter_detector = REC__Calorimeter->getByte("detector",row);
	REC__Calorimeter_sector = REC__Calorimeter->getByte("sector",row);
	REC__Calorimeter_layer = REC__Calorimeter->getByte("layer",row);
	REC__Calorimeter_energy = REC__Calorimeter->getFloat("energy",row);
	REC__Calorimeter_time = REC__Calorimeter->getFloat("time",row);
	REC__Calorimeter_path = REC__Calorimeter->getFloat("path",row);
	REC__Calorimeter_chi2 = REC__Calorimeter->getFloat("chi2",row);
	REC__Calorimeter_x = REC__Calorimeter->getFloat("x",row);
	REC__Calorimeter_y = REC__Calorimeter->getFloat("y",row);
	REC__Calorimeter_z = REC__Calorimeter->getFloat("z",row);
	REC__Calorimeter_hx = REC__Calorimeter->getFloat("hx",row);
	REC__Calorimeter_hy = REC__Calorimeter->getFloat("hy",row);
	REC__Calorimeter_hz = REC__Calorimeter->getFloat("hz",row);
	REC__Calorimeter_lu = REC__Calorimeter->getFloat("lu",row);
	REC__Calorimeter_lv = REC__Calorimeter->getFloat("lv",row);
	REC__Calorimeter_lw = REC__Calorimeter->getFloat("lw",row);
	REC__Calorimeter_du = REC__Calorimeter->getFloat("du",row);
	REC__Calorimeter_dv = REC__Calorimeter->getFloat("dv",row);
	REC__Calorimeter_dw = REC__Calorimeter->getFloat("dw",row);
	REC__Calorimeter_m2u = REC__Calorimeter->getFloat("m2u",row);
	REC__Calorimeter_m2v = REC__Calorimeter->getFloat("m2v",row);
	REC__Calorimeter_m2w = REC__Calorimeter->getFloat("m2w",row);
	REC__Calorimeter_m3u = REC__Calorimeter->getFloat("m3u",row);
	REC__Calorimeter_m3v = REC__Calorimeter->getFloat("m3v",row);
	REC__Calorimeter_m3w = REC__Calorimeter->getFloat("m3w",row);
	REC__Calorimeter_status = REC__Calorimeter->getShort("status",row);
	return 0;
} 

int get_REC__CovMat(int row){
	REC__CovMat_index = REC__CovMat->getShort("index",row);
	REC__CovMat_pindex = REC__CovMat->getShort("pindex",row);
	REC__CovMat_C11 = REC__CovMat->getFloat("C11",row);
	REC__CovMat_C12 = REC__CovMat->getFloat("C12",row);
	REC__CovMat_C13 = REC__CovMat->getFloat("C13",row);
	REC__CovMat_C14 = REC__CovMat->getFloat("C14",row);
	REC__CovMat_C15 = REC__CovMat->getFloat("C15",row);
	REC__CovMat_C22 = REC__CovMat->getFloat("C22",row);
	REC__CovMat_C23 = REC__CovMat->getFloat("C23",row);
	REC__CovMat_C24 = REC__CovMat->getFloat("C24",row);
	REC__CovMat_C25 = REC__CovMat->getFloat("C25",row);
	REC__CovMat_C33 = REC__CovMat->getFloat("C33",row);
	REC__CovMat_C34 = REC__CovMat->getFloat("C34",row);
	REC__CovMat_C35 = REC__CovMat->getFloat("C35",row);
	REC__CovMat_C44 = REC__CovMat->getFloat("C44",row);
	REC__CovMat_C45 = REC__CovMat->getFloat("C45",row);
	REC__CovMat_C55 = REC__CovMat->getFloat("C55",row);
	return 0;
} 

int get_RICH__response(int row){
	RICH__response_index = RICH__response->getShort("index",row);
	RICH__response_pindex = RICH__response->getShort("pindex",row);
	RICH__response_detector = RICH__response->getByte("detector",row);
	RICH__response_sector = RICH__response->getByte("sector",row);
	RICH__response_layer = RICH__response->getByte("layer",row);
	RICH__response_energy = RICH__response->getFloat("energy",row);
	RICH__response_time = RICH__response->getFloat("time",row);
	RICH__response_path = RICH__response->getFloat("path",row);
	RICH__response_chi2 = RICH__response->getFloat("chi2",row);
	RICH__response_x = RICH__response->getFloat("x",row);
	RICH__response_y = RICH__response->getFloat("y",row);
	RICH__response_z = RICH__response->getFloat("z",row);
	RICH__response_hx = RICH__response->getFloat("hx",row);
	RICH__response_hy = RICH__response->getFloat("hy",row);
	RICH__response_hz = RICH__response->getFloat("hz",row);
	RICH__response_status = RICH__response->getShort("status",row);
	return 0;
} 

int get_MC__Event(int row){
	MC__Event_npart = MC__Event->getShort("npart",row);
	MC__Event_atarget = MC__Event->getShort("atarget",row);
	MC__Event_ztarget = MC__Event->getShort("ztarget",row);
	MC__Event_ptarget = MC__Event->getFloat("ptarget",row);
	MC__Event_pbeam = MC__Event->getFloat("pbeam",row);
	MC__Event_btype = MC__Event->getShort("btype",row);
	MC__Event_ebeam = MC__Event->getFloat("ebeam",row);
	MC__Event_targetid = MC__Event->getShort("targetid",row);
	MC__Event_processid = MC__Event->getShort("processid",row);
	MC__Event_weight = MC__Event->getFloat("weight",row);
	return 0;
} 

int get_RAW__epics(int row){
	RAW__epics_json = RAW__epics->getByte("json",row);
	return 0;
} 

int get_RICH__clusters(int row){
	RICH__clusters_id = RICH__clusters->getShort("id",row);
	RICH__clusters_size = RICH__clusters->getShort("size",row);
	RICH__clusters_sector = RICH__clusters->getShort("sector",row);
	RICH__clusters_tile = RICH__clusters->getShort("tile",row);
	RICH__clusters_pmt = RICH__clusters->getShort("pmt",row);
	RICH__clusters_charge = RICH__clusters->getFloat("charge",row);
	RICH__clusters_time = RICH__clusters->getFloat("time",row);
	RICH__clusters_rawtime = RICH__clusters->getFloat("rawtime",row);
	RICH__clusters_x = RICH__clusters->getFloat("x",row);
	RICH__clusters_y = RICH__clusters->getFloat("y",row);
	RICH__clusters_z = RICH__clusters->getFloat("z",row);
	RICH__clusters_wtime = RICH__clusters->getFloat("wtime",row);
	RICH__clusters_wx = RICH__clusters->getFloat("wx",row);
	RICH__clusters_wy = RICH__clusters->getFloat("wy",row);
	RICH__clusters_wz = RICH__clusters->getFloat("wz",row);
	return 0;
} 

int get_REC__Scintillator(int row){
	REC__Scintillator_index = REC__Scintillator->getShort("index",row);
	REC__Scintillator_pindex = REC__Scintillator->getShort("pindex",row);
	REC__Scintillator_detector = REC__Scintillator->getByte("detector",row);
	REC__Scintillator_sector = REC__Scintillator->getByte("sector",row);
	REC__Scintillator_layer = REC__Scintillator->getByte("layer",row);
	REC__Scintillator_component = REC__Scintillator->getShort("component",row);
	REC__Scintillator_energy = REC__Scintillator->getFloat("energy",row);
	REC__Scintillator_time = REC__Scintillator->getFloat("time",row);
	REC__Scintillator_path = REC__Scintillator->getFloat("path",row);
	REC__Scintillator_chi2 = REC__Scintillator->getFloat("chi2",row);
	REC__Scintillator_x = REC__Scintillator->getFloat("x",row);
	REC__Scintillator_y = REC__Scintillator->getFloat("y",row);
	REC__Scintillator_z = REC__Scintillator->getFloat("z",row);
	REC__Scintillator_hx = REC__Scintillator->getFloat("hx",row);
	REC__Scintillator_hy = REC__Scintillator->getFloat("hy",row);
	REC__Scintillator_hz = REC__Scintillator->getFloat("hz",row);
	REC__Scintillator_status = REC__Scintillator->getShort("status",row);
	REC__Scintillator_dedx = REC__Scintillator->getFloat("dedx",row);
	return 0;
} 

int get_MC__Particle(int row){
	MC__Particle_pid = MC__Particle->getInt("pid",row);
	MC__Particle_px = MC__Particle->getFloat("px",row);
	MC__Particle_py = MC__Particle->getFloat("py",row);
	MC__Particle_pz = MC__Particle->getFloat("pz",row);
	MC__Particle_vx = MC__Particle->getFloat("vx",row);
	MC__Particle_vy = MC__Particle->getFloat("vy",row);
	MC__Particle_vz = MC__Particle->getFloat("vz",row);
	MC__Particle_vt = MC__Particle->getFloat("vt",row);
	return 0;
} 

int get_RICH__tdc(int row){
	RICH__tdc_sector = RICH__tdc->getByte("sector",row);
	RICH__tdc_layer = RICH__tdc->getByte("layer",row);
	RICH__tdc_component = RICH__tdc->getShort("component",row);
	RICH__tdc_order = RICH__tdc->getByte("order",row);
	RICH__tdc_TDC = RICH__tdc->getInt("TDC",row);
	return 0;
} 

int get_RUN__scaler(int row){
	RUN__scaler_fcupgated = RUN__scaler->getFloat("fcupgated",row);
	RUN__scaler_fcup = RUN__scaler->getFloat("fcup",row);
	RUN__scaler_livetime = RUN__scaler->getFloat("livetime",row);
	return 0;
} 

int get_RICH__hadrons(int row){
	RICH__hadrons_id = RICH__hadrons->getShort("id",row);
	RICH__hadrons_hit_index = RICH__hadrons->getShort("hit_index",row);
	RICH__hadrons_particle_index = RICH__hadrons->getShort("particle_index",row);
	RICH__hadrons_traced_the = RICH__hadrons->getFloat("traced_the",row);
	RICH__hadrons_traced_phi = RICH__hadrons->getFloat("traced_phi",row);
	RICH__hadrons_traced_hitx = RICH__hadrons->getFloat("traced_hitx",row);
	RICH__hadrons_traced_hity = RICH__hadrons->getFloat("traced_hity",row);
	RICH__hadrons_traced_hitz = RICH__hadrons->getFloat("traced_hitz",row);
	RICH__hadrons_traced_time = RICH__hadrons->getFloat("traced_time",row);
	RICH__hadrons_traced_path = RICH__hadrons->getFloat("traced_path",row);
	RICH__hadrons_traced_ilay = RICH__hadrons->getShort("traced_ilay",row);
	RICH__hadrons_traced_ico = RICH__hadrons->getShort("traced_ico",row);
	RICH__hadrons_traced_emix = RICH__hadrons->getFloat("traced_emix",row);
	RICH__hadrons_traced_emiy = RICH__hadrons->getFloat("traced_emiy",row);
	RICH__hadrons_traced_emiz = RICH__hadrons->getFloat("traced_emiz",row);
	RICH__hadrons_EtaC_ele = RICH__hadrons->getFloat("EtaC_ele",row);
	RICH__hadrons_EtaC_pi = RICH__hadrons->getFloat("EtaC_pi",row);
	RICH__hadrons_EtaC_k = RICH__hadrons->getFloat("EtaC_k",row);
	RICH__hadrons_EtaC_pr = RICH__hadrons->getFloat("EtaC_pr",row);
	RICH__hadrons_EtaC_min = RICH__hadrons->getFloat("EtaC_min",row);
	RICH__hadrons_EtaC_max = RICH__hadrons->getFloat("EtaC_max",row);
	return 0;
} 

int get_REC__Track(int row){
	REC__Track_index = REC__Track->getShort("index",row);
	REC__Track_pindex = REC__Track->getShort("pindex",row);
	REC__Track_detector = REC__Track->getByte("detector",row);
	REC__Track_sector = REC__Track->getByte("sector",row);
	REC__Track_status = REC__Track->getShort("status",row);
	REC__Track_q = REC__Track->getByte("q",row);
	REC__Track_chi2 = REC__Track->getFloat("chi2",row);
	REC__Track_NDF = REC__Track->getShort("NDF",row);
	return 0;
} 

int get_RICH__ringCher(int row){
	RICH__ringCher_id = RICH__ringCher->getShort("id",row);
	RICH__ringCher_hindex = RICH__ringCher->getShort("hindex",row);
	RICH__ringCher_pindex = RICH__ringCher->getByte("pindex",row);
	RICH__ringCher_pmt = RICH__ringCher->getShort("pmt",row);
	RICH__ringCher_anode = RICH__ringCher->getByte("anode",row);
	RICH__ringCher_time = RICH__ringCher->getFloat("time",row);
	RICH__ringCher_apath = RICH__ringCher->getFloat("apath",row);
	RICH__ringCher_atime = RICH__ringCher->getFloat("atime",row);
	RICH__ringCher_aEtaC = RICH__ringCher->getFloat("aEtaC",row);
	RICH__ringCher_tpath = RICH__ringCher->getFloat("tpath",row);
	RICH__ringCher_ttime = RICH__ringCher->getFloat("ttime",row);
	RICH__ringCher_tEtaC = RICH__ringCher->getFloat("tEtaC",row);
	RICH__ringCher_nrfl = RICH__ringCher->getByte("nrfl",row);
	RICH__ringCher_1rfl = RICH__ringCher->getShort("1rfl",row);
	return 0;
} 

int get_REC__ForwardTagger(int row){
	REC__ForwardTagger_index = REC__ForwardTagger->getShort("index",row);
	REC__ForwardTagger_pindex = REC__ForwardTagger->getShort("pindex",row);
	REC__ForwardTagger_detector = REC__ForwardTagger->getByte("detector",row);
	REC__ForwardTagger_layer = REC__ForwardTagger->getByte("layer",row);
	REC__ForwardTagger_energy = REC__ForwardTagger->getFloat("energy",row);
	REC__ForwardTagger_time = REC__ForwardTagger->getFloat("time",row);
	REC__ForwardTagger_path = REC__ForwardTagger->getFloat("path",row);
	REC__ForwardTagger_chi2 = REC__ForwardTagger->getFloat("chi2",row);
	REC__ForwardTagger_x = REC__ForwardTagger->getFloat("x",row);
	REC__ForwardTagger_y = REC__ForwardTagger->getFloat("y",row);
	REC__ForwardTagger_z = REC__ForwardTagger->getFloat("z",row);
	REC__ForwardTagger_dx = REC__ForwardTagger->getFloat("dx",row);
	REC__ForwardTagger_dy = REC__ForwardTagger->getFloat("dy",row);
	REC__ForwardTagger_radius = REC__ForwardTagger->getFloat("radius",row);
	REC__ForwardTagger_size = REC__ForwardTagger->getShort("size",row);
	REC__ForwardTagger_status = REC__ForwardTagger->getShort("status",row);
	return 0;
} 

int get_RICH__hadCher(int row){
	RICH__hadCher_id = RICH__hadCher->getByte("id",row);
	RICH__hadCher_hindex = RICH__hadCher->getByte("hindex",row);
	RICH__hadCher_pindex = RICH__hadCher->getByte("pindex",row);
	RICH__hadCher_emilay = RICH__hadCher->getByte("emilay",row);
	RICH__hadCher_emico = RICH__hadCher->getByte("emico",row);
	RICH__hadCher_enico = RICH__hadCher->getByte("enico",row);
	RICH__hadCher_emqua = RICH__hadCher->getShort("emqua",row);
	RICH__hadCher_mchi2 = RICH__hadCher->getFloat("mchi2",row);
	RICH__hadCher_ch_min = RICH__hadCher->getFloat("ch_min",row);
	RICH__hadCher_ch_max = RICH__hadCher->getFloat("ch_max",row);
	RICH__hadCher_dt_max = RICH__hadCher->getFloat("dt_max",row);
	RICH__hadCher_ch_dir = RICH__hadCher->getFloat("ch_dir",row);
	RICH__hadCher_ch_lat = RICH__hadCher->getFloat("ch_lat",row);
	RICH__hadCher_ch_spe = RICH__hadCher->getFloat("ch_spe",row);
	RICH__hadCher_best_PID = RICH__hadCher->getByte("best_PID",row);
	RICH__hadCher_RQ_prob = RICH__hadCher->getFloat("RQ_prob",row);
	RICH__hadCher_el_prob = RICH__hadCher->getFloat("el_prob",row);
	RICH__hadCher_pi_prob = RICH__hadCher->getFloat("pi_prob",row);
	RICH__hadCher_k_prob = RICH__hadCher->getFloat("k_prob",row);
	RICH__hadCher_pr_prob = RICH__hadCher->getFloat("pr_prob",row);
	return 0;
} 

int get_REC__Cherenkov(int row){
	REC__Cherenkov_index = REC__Cherenkov->getShort("index",row);
	REC__Cherenkov_pindex = REC__Cherenkov->getShort("pindex",row);
	REC__Cherenkov_detector = REC__Cherenkov->getByte("detector",row);
	REC__Cherenkov_sector = REC__Cherenkov->getByte("sector",row);
	REC__Cherenkov_nphe = REC__Cherenkov->getFloat("nphe",row);
	REC__Cherenkov_time = REC__Cherenkov->getFloat("time",row);
	REC__Cherenkov_path = REC__Cherenkov->getFloat("path",row);
	REC__Cherenkov_chi2 = REC__Cherenkov->getFloat("chi2",row);
	REC__Cherenkov_x = REC__Cherenkov->getFloat("x",row);
	REC__Cherenkov_y = REC__Cherenkov->getFloat("y",row);
	REC__Cherenkov_z = REC__Cherenkov->getFloat("z",row);
	REC__Cherenkov_dtheta = REC__Cherenkov->getFloat("dtheta",row);
	REC__Cherenkov_dphi = REC__Cherenkov->getFloat("dphi",row);
	REC__Cherenkov_status = REC__Cherenkov->getShort("status",row);
	return 0;
} 

int get_RICH__photons(int row){
	RICH__photons_id = RICH__photons->getShort("id",row);
	RICH__photons_type = RICH__photons->getShort("type",row);
	RICH__photons_hit_index = RICH__photons->getShort("hit_index",row);
	RICH__photons_hadron_index = RICH__photons->getShort("hadron_index",row);
	RICH__photons_start_time = RICH__photons->getFloat("start_time",row);
	RICH__photons_analytic_the = RICH__photons->getFloat("analytic_the",row);
	RICH__photons_analytic_phi = RICH__photons->getFloat("analytic_phi",row);
	RICH__photons_analytic_path = RICH__photons->getFloat("analytic_path",row);
	RICH__photons_analytic_time = RICH__photons->getFloat("analytic_time",row);
	RICH__photons_analytic_EtaC = RICH__photons->getFloat("analytic_EtaC",row);
	RICH__photons_analytic_aeron = RICH__photons->getFloat("analytic_aeron",row);
	RICH__photons_analytic_elpr = RICH__photons->getFloat("analytic_elpr",row);
	RICH__photons_analytic_pipr = RICH__photons->getFloat("analytic_pipr",row);
	RICH__photons_analytic_kpr = RICH__photons->getFloat("analytic_kpr",row);
	RICH__photons_analytic_prpr = RICH__photons->getFloat("analytic_prpr",row);
	RICH__photons_analytic_bgpr = RICH__photons->getFloat("analytic_bgpr",row);
	RICH__photons_traced_the = RICH__photons->getFloat("traced_the",row);
	RICH__photons_traced_phi = RICH__photons->getFloat("traced_phi",row);
	RICH__photons_traced_hitx = RICH__photons->getFloat("traced_hitx",row);
	RICH__photons_traced_hity = RICH__photons->getFloat("traced_hity",row);
	RICH__photons_traced_hitz = RICH__photons->getFloat("traced_hitz",row);
	RICH__photons_traced_path = RICH__photons->getFloat("traced_path",row);
	RICH__photons_traced_time = RICH__photons->getFloat("traced_time",row);
	RICH__photons_traced_nrfl = RICH__photons->getShort("traced_nrfl",row);
	RICH__photons_traced_nrfr = RICH__photons->getShort("traced_nrfr",row);
	RICH__photons_traced_1rfl = RICH__photons->getShort("traced_1rfl",row);
	RICH__photons_traced_EtaC = RICH__photons->getFloat("traced_EtaC",row);
	RICH__photons_traced_aeron = RICH__photons->getFloat("traced_aeron",row);
	RICH__photons_traced_elpr = RICH__photons->getFloat("traced_elpr",row);
	RICH__photons_traced_pipr = RICH__photons->getFloat("traced_pipr",row);
	RICH__photons_traced_kpr = RICH__photons->getFloat("traced_kpr",row);
	RICH__photons_traced_prpr = RICH__photons->getFloat("traced_prpr",row);
	RICH__photons_traced_bgpr = RICH__photons->getFloat("traced_bgpr",row);
	return 0;
} 

int get_RECFT__Particle(int row){
	RECFT__Particle_pid = RECFT__Particle->getInt("pid",row);
	RECFT__Particle_vt = RECFT__Particle->getFloat("vt",row);
	RECFT__Particle_beta = RECFT__Particle->getFloat("beta",row);
	RECFT__Particle_chi2pid = RECFT__Particle->getFloat("chi2pid",row);
	RECFT__Particle_status = RECFT__Particle->getShort("status",row);
	return 0;
} 

int get_HEL__flip(int row){
	HEL__flip_run = HEL__flip->getInt("run",row);
	HEL__flip_event = HEL__flip->getInt("event",row);
	HEL__flip_timestamp = HEL__flip->getLong("timestamp",row);
	HEL__flip_helicity = HEL__flip->getByte("helicity",row);
	HEL__flip_helicityRaw = HEL__flip->getByte("helicityRaw",row);
	HEL__flip_pair = HEL__flip->getByte("pair",row);
	HEL__flip_pattern = HEL__flip->getByte("pattern",row);
	HEL__flip_status = HEL__flip->getByte("status",row);
	return 0;
} 

int get_RECFT__Event(int row){
	RECFT__Event_category = RECFT__Event->getLong("category",row);
	RECFT__Event_startTime = RECFT__Event->getFloat("startTime",row);
	return 0;
} 

int get_MC__Lund(int row){
	MC__Lund_index = MC__Lund->getByte("index",row);
	MC__Lund_lifetime = MC__Lund->getFloat("lifetime",row);
	MC__Lund_type = MC__Lund->getByte("type",row);
	MC__Lund_pid = MC__Lund->getInt("pid",row);
	MC__Lund_parent = MC__Lund->getByte("parent",row);
	MC__Lund_daughter = MC__Lund->getByte("daughter",row);
	MC__Lund_px = MC__Lund->getFloat("px",row);
	MC__Lund_py = MC__Lund->getFloat("py",row);
	MC__Lund_pz = MC__Lund->getFloat("pz",row);
	MC__Lund_energy = MC__Lund->getFloat("energy",row);
	MC__Lund_mass = MC__Lund->getFloat("mass",row);
	MC__Lund_vx = MC__Lund->getFloat("vx",row);
	MC__Lund_vy = MC__Lund->getFloat("vy",row);
	MC__Lund_vz = MC__Lund->getFloat("vz",row);
	return 0;
} 

int InitBanks(){

	if (fFactory->hasSchema("MC::Header"))
		MC__Header = new hipo::bank(fFactory->getSchema("MC::Header"));
	if (fFactory->hasSchema("RAW::scaler"))
		RAW__scaler = new hipo::bank(fFactory->getSchema("RAW::scaler"));
	if (fFactory->hasSchema("HEL::online"))
		HEL__online = new hipo::bank(fFactory->getSchema("HEL::online"));
	if (fFactory->hasSchema("REC::Event"))
		REC__Event = new hipo::bank(fFactory->getSchema("REC::Event"));
	if (fFactory->hasSchema("REC::Particle"))
		REC__Particle = new hipo::bank(fFactory->getSchema("REC::Particle"));
	if (fFactory->hasSchema("RUN::config"))
		RUN__config = new hipo::bank(fFactory->getSchema("RUN::config"));
	if (fFactory->hasSchema("REC::Traj"))
		REC__Traj = new hipo::bank(fFactory->getSchema("REC::Traj"));
	if (fFactory->hasSchema("RICH::hits"))
		RICH__hits = new hipo::bank(fFactory->getSchema("RICH::hits"));
	if (fFactory->hasSchema("MC::True"))
		MC__True = new hipo::bank(fFactory->getSchema("MC::True"));
	if (fFactory->hasSchema("REC::Calorimeter"))
		REC__Calorimeter = new hipo::bank(fFactory->getSchema("REC::Calorimeter"));
	if (fFactory->hasSchema("REC::CovMat"))
		REC__CovMat = new hipo::bank(fFactory->getSchema("REC::CovMat"));
	if (fFactory->hasSchema("RICH::response"))
		RICH__response = new hipo::bank(fFactory->getSchema("RICH::response"));
	if (fFactory->hasSchema("MC::Event"))
		MC__Event = new hipo::bank(fFactory->getSchema("MC::Event"));
	if (fFactory->hasSchema("RAW::epics"))
		RAW__epics = new hipo::bank(fFactory->getSchema("RAW::epics"));
	if (fFactory->hasSchema("RICH::clusters"))
		RICH__clusters = new hipo::bank(fFactory->getSchema("RICH::clusters"));
	if (fFactory->hasSchema("REC::Scintillator"))
		REC__Scintillator = new hipo::bank(fFactory->getSchema("REC::Scintillator"));
	if (fFactory->hasSchema("MC::Particle"))
		MC__Particle = new hipo::bank(fFactory->getSchema("MC::Particle"));
	if (fFactory->hasSchema("RICH::tdc"))
		RICH__tdc = new hipo::bank(fFactory->getSchema("RICH::tdc"));
	if (fFactory->hasSchema("RUN::scaler"))
		RUN__scaler = new hipo::bank(fFactory->getSchema("RUN::scaler"));
	if (fFactory->hasSchema("RICH::hadrons"))
		RICH__hadrons = new hipo::bank(fFactory->getSchema("RICH::hadrons"));
	if (fFactory->hasSchema("REC::Track"))
		REC__Track = new hipo::bank(fFactory->getSchema("REC::Track"));
	if (fFactory->hasSchema("RICH::ringCher"))
		RICH__ringCher = new hipo::bank(fFactory->getSchema("RICH::ringCher"));
	if (fFactory->hasSchema("REC::ForwardTagger"))
		REC__ForwardTagger = new hipo::bank(fFactory->getSchema("REC::ForwardTagger"));
	if (fFactory->hasSchema("RICH::hadCher"))
		RICH__hadCher = new hipo::bank(fFactory->getSchema("RICH::hadCher"));
	if (fFactory->hasSchema("REC::Cherenkov"))
		REC__Cherenkov = new hipo::bank(fFactory->getSchema("REC::Cherenkov"));
	if (fFactory->hasSchema("RICH::photons"))
		RICH__photons = new hipo::bank(fFactory->getSchema("RICH::photons"));
	if (fFactory->hasSchema("RECFT::Particle"))
		RECFT__Particle = new hipo::bank(fFactory->getSchema("RECFT::Particle"));
	if (fFactory->hasSchema("HEL::flip"))
		HEL__flip = new hipo::bank(fFactory->getSchema("HEL::flip"));
	if (fFactory->hasSchema("RECFT::Event"))
		RECFT__Event = new hipo::bank(fFactory->getSchema("RECFT::Event"));
	if (fFactory->hasSchema("MC::Lund"))
		MC__Lund = new hipo::bank(fFactory->getSchema("MC::Lund"));

	return 1;
}

int FillBanks(){
	if (fFactory->hasSchema("MC::Header"))
		 fEvent->getStructure(*MC__Header);
	if (fFactory->hasSchema("RAW::scaler"))
		 fEvent->getStructure(*RAW__scaler);
	if (fFactory->hasSchema("HEL::online"))
		 fEvent->getStructure(*HEL__online);
	if (fFactory->hasSchema("REC::Event"))
		 fEvent->getStructure(*REC__Event);
	if (fFactory->hasSchema("REC::Particle"))
		 fEvent->getStructure(*REC__Particle);
	if (fFactory->hasSchema("RUN::config"))
		 fEvent->getStructure(*RUN__config);
	if (fFactory->hasSchema("REC::Traj"))
		 fEvent->getStructure(*REC__Traj);
	if (fFactory->hasSchema("RICH::hits"))
		 fEvent->getStructure(*RICH__hits);
	if (fFactory->hasSchema("MC::True"))
		 fEvent->getStructure(*MC__True);
	if (fFactory->hasSchema("REC::Calorimeter"))
		 fEvent->getStructure(*REC__Calorimeter);
	if (fFactory->hasSchema("REC::CovMat"))
		 fEvent->getStructure(*REC__CovMat);
	if (fFactory->hasSchema("RICH::response"))
		 fEvent->getStructure(*RICH__response);
	if (fFactory->hasSchema("MC::Event"))
		 fEvent->getStructure(*MC__Event);
	if (fFactory->hasSchema("RAW::epics"))
		 fEvent->getStructure(*RAW__epics);
	if (fFactory->hasSchema("RICH::clusters"))
		 fEvent->getStructure(*RICH__clusters);
	if (fFactory->hasSchema("REC::Scintillator"))
		 fEvent->getStructure(*REC__Scintillator);
	if (fFactory->hasSchema("MC::Particle"))
		 fEvent->getStructure(*MC__Particle);
	if (fFactory->hasSchema("RICH::tdc"))
		 fEvent->getStructure(*RICH__tdc);
	if (fFactory->hasSchema("RUN::scaler"))
		 fEvent->getStructure(*RUN__scaler);
	if (fFactory->hasSchema("RICH::hadrons"))
		 fEvent->getStructure(*RICH__hadrons);
	if (fFactory->hasSchema("REC::Track"))
		 fEvent->getStructure(*REC__Track);
	if (fFactory->hasSchema("RICH::ringCher"))
		 fEvent->getStructure(*RICH__ringCher);
	if (fFactory->hasSchema("REC::ForwardTagger"))
		 fEvent->getStructure(*REC__ForwardTagger);
	if (fFactory->hasSchema("RICH::hadCher"))
		 fEvent->getStructure(*RICH__hadCher);
	if (fFactory->hasSchema("REC::Cherenkov"))
		 fEvent->getStructure(*REC__Cherenkov);
	if (fFactory->hasSchema("RICH::photons"))
		 fEvent->getStructure(*RICH__photons);
	if (fFactory->hasSchema("RECFT::Particle"))
		 fEvent->getStructure(*RECFT__Particle);
	if (fFactory->hasSchema("HEL::flip"))
		 fEvent->getStructure(*HEL__flip);
	if (fFactory->hasSchema("RECFT::Event"))
		 fEvent->getStructure(*RECFT__Event);
	if (fFactory->hasSchema("MC::Lund"))
		 fEvent->getStructure(*MC__Lund);

	return 1;
}

